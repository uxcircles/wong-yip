/* Wong & Yip concept: menu, Stamp Duty calculator, live HMRC dates, contact form, lazy map. */
(() => {
  const zh = document.documentElement.lang.startsWith('zh');
  const T = (en, z) => (zh ? z : en);
  const gbp = (n) => '£' + Math.round(n).toLocaleString('en-GB');

  /* ---------- menu ---------- */
  const btn = document.querySelector('.menu-btn');
  const menu = document.getElementById('menu');
  if (btn && menu) {
    const set = (open) => {
      btn.setAttribute('aria-expanded', open);
      menu.hidden = !open;
      document.body.classList.toggle('menu-open', open);
      btn.textContent = open ? T('Close', '關閉') : T('Menu', '選單');
    };
    btn.addEventListener('click', () => set(menu.hidden));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { set(false); btn.focus(); } });
    window.matchMedia('(min-width: 1021px)').addEventListener('change', (m) => { if (m.matches) set(false); });
  }

  /* ---------- Stamp Duty (England & NI, residential, from 1 April 2025) ---------- */
  const STD = [[125000, 0], [250000, 0.02], [925000, 0.05], [1500000, 0.10], [Infinity, 0.12]];
  const FTB = [[300000, 0], [500000, 0.05]];
  const band = (lo, hi) => (hi === Infinity ? T(`Over ${gbp(lo)}`, `${gbp(lo)} 以上`) : `${gbp(lo === 0 ? 0 : lo + 1)} – ${gbp(hi)}`);

  function sdlt(price, type, nonres) {
    const notes = [];
    let bands = STD;
    let extra = 0;
    if (type === 'ftb') {
      if (price <= 500000) bands = FTB;
      else notes.push(T('Over £500,000 there is no first-time buyer relief, so standard rates apply.', '樓價超過 £500,000，不能使用首次置業寬減，須按一般稅率計算。'));
    }
    if (type === 'add') {
      if (price >= 40000) {
        extra += 0.05;
        notes.push(T('Includes the 5% higher rates. If this replaces your main home and you sell the old one within 36 months, you can claim the 5% back.', '已包括 5% 額外物業附加。如新物業取代你的主要住所，並在 36 個月內賣出舊居，可申請退回這 5%。'));
      } else notes.push(T('Under £40,000 the higher rates do not apply.', '樓價低於 £40,000，不須付額外物業附加。'));
    }
    if (nonres) {
      extra += 0.02;
      notes.push(T('Includes the 2% non-resident surcharge. Spend 183 days in the UK in a 365-day period around the purchase and you can usually claim it back.', '已包括 2% 非居民附加費。如在購買前後的 365 日內在英國住滿 183 日，一般可申請退回。'));
    }
    if (type === 'home' || type === 'ftb') notes.push(T('A home you own in Hong Kong or anywhere else counts. Still own one? Choose “More than one home”.', '在香港或其他地方擁有的物業也會計算在內。如仍持有，請選「多於一個物業」。'));
    const rows = [];
    let lo = 0;
    let total = 0;
    for (const [hi, r] of bands) {
      if (price <= lo) break;
      const part = Math.min(price, hi) - lo;
      const rate = r + extra;
      const tax = part * rate;
      total += tax;
      rows.push([band(lo, hi), (Math.round(rate * 1000) / 10) + '%', tax]);
      lo = hi;
    }
    return { rows, total: Math.floor(total), notes };
  }

  document.querySelectorAll('[data-sdlt]').forEach((form) => {
    const input = form.elements.price;
    const out = {
      rows: form.querySelector('[data-rows]'), total: form.querySelector('[data-total]'),
      eff: form.querySelector('[data-eff]'), notes: form.querySelector('[data-notes]'),
    };
    const run = () => {
      const price = Number(String(input.value).replace(/[^\d.]/g, '')) || 0;
      const r = sdlt(price, form.elements.type.value, form.elements.nonres.checked);
      out.total.textContent = gbp(r.total);
      out.eff.textContent = price ? T(`${(r.total / price * 100).toFixed(2)}% of ${gbp(price)}`, `相當於樓價 ${gbp(price)} 的 ${(r.total / price * 100).toFixed(2)}%`) : T('Enter a price', '請輸入樓價');
      out.rows.innerHTML = r.rows.map(([b, rate, tax]) => `<tr><td>${b}</td><td>${rate}</td><td>${gbp(tax)}</td></tr>`).join('');
      out.notes.innerHTML = r.notes.map((n) => `<p>${n}</p>`).join('');
      // WhatsApp links on this page carry the estimate, so the accountant sees the case straight away
      const type = { ftb: T('My first home ever', '首次置業'), home: T('Only this home', '只有這一個物業'), add: T('More than one home', '多於一個物業') }[form.elements.type.value];
      const msg = T(
        `Hello, I would like you to check my Stamp Duty.\nPrice: ${gbp(price)}\nAfter buying I will own: ${type}\nNon-UK resident: ${form.elements.nonres.checked ? 'Yes' : 'No'}\nWebsite estimate: ${gbp(r.total)}`,
        `你好，想請你們確認我的印花稅：\n樓價：${gbp(price)}\n買入後：${type}\n非英國居民：${form.elements.nonres.checked ? '是' : '否'}\n網站估算：${gbp(r.total)}`);
      if (price) document.querySelectorAll('[data-wa-sdlt]').forEach((a) => { a.href = 'https://wa.me/447599614875?text=' + encodeURIComponent(msg); });
    };
    input.addEventListener('input', () => {
      const digits = input.value.replace(/\D/g, '').slice(0, 9);
      const pos = input.value.length - input.selectionStart;
      input.value = digits ? Number(digits).toLocaleString('en-GB') : '';
      const p = Math.max(0, input.value.length - pos);
      try { input.setSelectionRange(p, p); } catch (e) { /* ignore */ }
      run();
    });
    form.addEventListener('change', run);
    form.addEventListener('submit', (e) => e.preventDefault());
    run();
  });

  /* ---------- HMRC dates, computed from today in London ---------- */
  const list = document.querySelector('[data-deadlines]');
  if (list) {
    const parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', year: 'numeric', month: 'numeric', day: 'numeric' }).formatToParts(new Date());
    const g = (t) => Number(parts.find((x) => x.type === t).value);
    const today = Date.UTC(g('year'), g('month') - 1, g('day'));
    const y0 = g('year');
    const ev = [];
    const ty = (y) => `${y}/${String(y + 1).slice(2)}`;
    for (let y = y0 - 1; y <= y0 + 1; y++) {
      ev.push([y, 0, 31, T(`Online Self Assessment return for ${ty(y - 2)} and tax due`, `${ty(y - 2)} 年度網上自我評估報稅及繳稅截止`)]);
      ev.push([y, 6, 31, T(`Second payment on account for ${ty(y - 1)}`, `${ty(y - 1)} 年度第二期預繳稅款`)]);
      ev.push([y, 9, 5, T(`Register for Self Assessment if you started self-employment or letting in ${ty(y - 1)}`, `${ty(y - 1)} 年度新自僱或新出租，登記自我評估`)]);
      ev.push([y, 9, 31, T(`Paper Self Assessment return for ${ty(y - 1)}`, `${ty(y - 1)} 年度紙本報稅表截止`)]);
      ev.push([y, 3, 6, T(`Tax year ${ty(y)} begins`, `${ty(y)} 稅務年度開始`)]);
      if (y >= 2026) {
        [[7, 7, 'Q1'], [10, 7, 'Q2'], [1, 7, 'Q3'], [4, 7, 'Q4']].forEach(([m, d, q]) => {
          const taxYear = m >= 7 ? y : y - 1;
          if (taxYear >= 2026) ev.push([y, m, d, T(`Making Tax Digital ${q} update, ${ty(taxYear)}`, `Making Tax Digital ${ty(taxYear)} 第 ${q.slice(1)} 季更新`)]);
        });
      }
    }
    const months = zh ? ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'] : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const next = ev.map(([y, m, d, w]) => ({ t: Date.UTC(y, m, d), y, m, d, w })).filter((e) => e.t >= today).sort((a, b) => a.t - b.t).slice(0, 4);
    list.innerHTML = next.map((e) => {
      const days = Math.round((e.t - today) / 864e5);
      const left = days === 0 ? T('Today', '今天') : T(`${days} day${days > 1 ? 's' : ''} to go`, `還有 ${days} 日`);
      return `<li><span class="d-day">${e.d}</span><span class="d-mon">${months[e.m]} ${e.y}</span><span class="d-what">${e.w}</span><span class="d-left">${left}</span></li>`;
    }).join('');
  }

  /* ---------- contact form: WhatsApp or email, nothing stored ---------- */
  document.querySelectorAll('[data-ask]').forEach((form) => {
    const err = form.querySelector('[data-err]');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const f = form.elements;
      let ok = true;
      ['name', 'reach', 'msg'].forEach((k) => {
        const bad = !f[k].value.trim();
        f[k].setAttribute('aria-invalid', bad);
        if (bad) ok = false;
      });
      err.hidden = ok;
      if (!ok) { form.querySelector('[aria-invalid="true"]').focus(); return; }
      const text = `${f.msg.value.trim()}\n\n${T('Name', '名字')}: ${f.name.value.trim()}\n${T('Contact', '聯絡')}: ${f.reach.value.trim()}\n${T('About', '服務')}: ${f.topic.value}`;
      const via = e.submitter && e.submitter.value;
      if (via === 'mail') location.href = `mailto:info@wongyipaccountants.co.uk?subject=${encodeURIComponent(T('Enquiry: ', '查詢：') + f.topic.value)}&body=${encodeURIComponent(text)}`;
      else window.open(`https://wa.me/447599614875?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
    });
  });

  /* ---------- map, loaded when it nears the screen ---------- */
  const box = document.querySelector('[data-map]');
  if (box && 'IntersectionObserver' in window) {
    const load = (src, tag) => new Promise((ok, bad) => {
      const el = document.createElement(tag === 'css' ? 'link' : 'script');
      if (tag === 'css') { el.rel = 'stylesheet'; el.href = src; } else { el.src = src; }
      el.onload = ok; el.onerror = bad;
      document.head.appendChild(el);
    });
    const io = new IntersectionObserver((entries) => {
      if (!entries.some((e) => e.isIntersecting)) return;
      io.disconnect();
      Promise.all([load(box.dataset.css, 'css'), load(box.dataset.src)])
        .then(() => load(box.dataset.mapjs))
        .then(() => window.wyMap && window.wyMap(box))
        .catch(() => { /* the sketch stays */ });
    }, { rootMargin: '400px' });
    io.observe(box);
  }
})();
