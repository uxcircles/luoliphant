(function () {
  "use strict";
  var zh = /^zh/.test(document.documentElement.lang);

  // Mobile menu
  var btn = document.querySelector(".menu-btn");
  var nav = document.getElementById("main-nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("open", !open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { btn.click(); btn.focus(); }
    });
  }

  // London / Beijing clocks
  var clocks = document.querySelectorAll(".clock");
  function tick() {
    var now = new Date();
    clocks.forEach(function (el) {
      var tz = el.getAttribute("data-tz");
      try {
        el.querySelector(".clock-time").textContent = new Intl.DateTimeFormat("en-GB", { hour: "2-digit", minute: "2-digit", hour12: false, timeZone: tz }).format(now);
        el.querySelector(".clock-day").textContent = new Intl.DateTimeFormat(zh ? document.documentElement.lang : "en-GB", { weekday: "long", day: "numeric", month: "short", timeZone: tz }).format(now);
      } catch (err) { /* very old browsers: leave placeholder */ }
    });
  }
  if (clocks.length) { tick(); setInterval(tick, 15000); }

  // Conveyancing fee calculator
  var calc = document.querySelector(".calc");
  if (calc) {
    var data = JSON.parse(calc.getAttribute("data-calc"));
    var limits = [500000, 1000000, 1500000, 2000000, 3000000];
    var type = document.getElementById("calc-type");
    var price = document.getElementById("calc-price");
    var fmt = function (n) { return "£" + Math.round(n).toLocaleString("en-GB"); };
    var run = function () {
      var p = parseFloat(String(price.value).replace(/[^0-9.]/g, ""));
      var out = ["calc-fee", "calc-vat", "calc-total"].map(function (id) { return document.getElementById(id); });
      if (!p || p <= 0) { out.forEach(function (o) { o.textContent = "—"; }); return; }
      var t = data[type.value], fee = null;
      for (var i = 0; i < limits.length; i++) { if (p < limits[i] || (i > 0 && p === limits[i])) { fee = t.fees[i]; break; } }
      if (p < limits[0]) fee = t.fees[0];
      if (fee === null) fee = p * t.pct / 100;
      out[0].textContent = fmt(fee);
      out[1].textContent = fmt(fee * 0.2);
      out[2].textContent = fmt(fee * 1.2);
    };
    price.addEventListener("input", run);
    price.addEventListener("blur", function () {
      var p = parseFloat(String(price.value).replace(/[^0-9.]/g, ""));
      if (p) price.value = Math.round(p).toLocaleString("en-GB");
    });
    type.addEventListener("change", run);
    run();
  }

  // Highlight the section in view (services index, fee tabs)
  var trackers = document.querySelectorAll(".side-index a, .fee-nav a");
  if (trackers.length && "IntersectionObserver" in window) {
    var map = {};
    trackers.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          trackers.forEach(function (a) { a.classList.remove("active"); });
          map[en.target.id].classList.add("active");
          if (map[en.target.id].parentElement.classList.contains("wrap")) {
            map[en.target.id].scrollIntoView({ block: "nearest", inline: "center" });
          }
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    Object.keys(map).forEach(function (id) { var s = document.getElementById(id); if (s) io.observe(s); });
  }

  // Testimonial filter
  var chips = document.querySelectorAll(".chip[data-filter]");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var f = c.getAttribute("data-filter");
      chips.forEach(function (x) { x.setAttribute("aria-pressed", String(x === c)); });
      document.querySelectorAll(".quotes-wall .quote").forEach(function (q) {
        q.hidden = !(f === "all" || q.getAttribute("data-matter") === f);
      });
    });
  });

  // Enquiry form -> pre-filled email (no backend)
  var form = document.getElementById("enquiry");
  if (form) {
    var params = new URLSearchParams(location.search);
    if (params.get("matter")) form.elements.matter.value = params.get("matter");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var req = ["name", "email", "situation", "goal"], bad = [];
      req.forEach(function (n) {
        var el = form.elements[n], ok = el.value.trim() && (n !== "email" || /.+@.+\..+/.test(el.value));
        el.classList.toggle("invalid", !ok);
        if (!ok) bad.push(el);
      });
      form.querySelector(".form-error").hidden = !bad.length;
      if (bad.length) { bad[0].focus(); return; }
      var m = form.elements.matter;
      var matter = m.value ? m.options[m.selectedIndex].text : "";
      var L = zh
        ? { n: "姓名", e: "電郵", p: "電話／微信", l: "語言", m: "法律範疇", s: "目前的情況", g: "希望達成的目標" }
        : { n: "Name", e: "Email", p: "Phone / WeChat", l: "Language", m: "Area of law", s: "Current situation", g: "What I want to achieve" };
      var lines = [
        L.n + ": " + form.elements.name.value.trim(),
        L.e + ": " + form.elements.email.value.trim(),
        L.p + ": " + (form.elements.phone.value.trim() || "-"),
        L.l + ": " + form.elements.language.value,
        L.m + ": " + (matter || "-"),
        "",
        L.s + ":",
        form.elements.situation.value.trim(),
        "",
        L.g + ":",
        form.elements.goal.value.trim()
      ];
      var subject = form.getAttribute("data-subject") + (matter ? " · " + matter : "");
      location.href = "mailto:" + form.getAttribute("data-email") + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
    });
  }
})();
