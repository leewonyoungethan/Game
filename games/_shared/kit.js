/* 앱개발부 게임 공통 도구: 저장, 효과음, 토스트, 화면, 캔버스 맞추기. 전역 Kit 하나만 만든다. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);

  // ---------------------------------------------------------------- storage (never throws)
  const store = {
    get(key, def = null) { try { const v = localStorage.getItem(key); return v === null ? def : JSON.parse(v); } catch (e) { return def; } },
    set(key, val) { try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {} },
  };
  /** best-score helper: Kit.best('key').get(), .submit(score) -> true when it is a new record */
  function best(key, lowerIsBetter = false) {
    return {
      get: () => store.get(key, null),
      submit(v) {
        const cur = store.get(key, null);
        const better = cur === null || (lowerIsBetter ? v < cur : v > cur);
        if (better) store.set(key, v);
        return better;
      },
    };
  }

  // ---------------------------------------------------------------- audio
  let AC = null, muted = store.get('kit_muted', false);
  function initAudio() {
    if (!AC) { try { AC = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { AC = null; } }
    if (AC && AC.state === 'suspended') AC.resume();
  }
  function tone(f, d = .15, type = 'sine', v = .07, slide = 0, delay = 0) {
    if (!AC || muted) return;
    const t = AC.currentTime + delay, o = AC.createOscillator(), g = AC.createGain();
    o.type = type; o.frequency.setValueAtTime(f, t);
    if (slide) o.frequency.exponentialRampToValueAtTime(Math.max(30, f + slide), t + d);
    g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(v, t + .008); g.gain.exponentialRampToValueAtTime(.0001, t + d);
    o.connect(g); g.connect(AC.destination); o.start(t); o.stop(t + d + .03);
  }
  function noise(d = .15, v = .08, freq = 1200, delay = 0) {
    if (!AC || muted) return;
    const n = Math.max(1, AC.sampleRate * d | 0), buf = AC.createBuffer(1, n, AC.sampleRate), x = buf.getChannelData(0);
    for (let i = 0; i < n; i++) x[i] = (Math.random() * 2 - 1) * (1 - i / n);
    const s = AC.createBufferSource(), fl = AC.createBiquadFilter(), g = AC.createGain();
    fl.type = 'lowpass'; fl.frequency.value = freq; g.gain.value = v;
    s.buffer = buf; s.connect(fl); fl.connect(g); g.connect(AC.destination); s.start(AC.currentTime + delay);
  }
  function chord(freqs, step = .07, type = 'triangle', v = .06, d = .2) { freqs.forEach((f, i) => tone(f, d, type, v, 0, i * step)); }
  function bindMute(btn) {
    const paint = () => { btn.textContent = muted ? '🔇 소리 꺼짐' : '🔊 소리 켜짐'; btn.setAttribute('aria-pressed', String(!muted)); };
    btn.addEventListener('click', () => { initAudio(); muted = !muted; store.set('kit_muted', muted); paint(); });
    paint();
  }
  addEventListener('pointerdown', initAudio, { capture: true });
  addEventListener('keydown', initAudio, { capture: true });

  // ---------------------------------------------------------------- toast & screens
  let toastEl = null, toastT = 0;
  function toast(msg, ms = 1300) {
    if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'toast'; toastEl.setAttribute('role', 'status'); document.body.append(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add('show');
    clearTimeout(toastT); toastT = setTimeout(() => toastEl.classList.remove('show'), ms);
  }
  function show(id) { const el = $(id); el.hidden = false; const f = el.querySelector('button.go, button, a'); if (f) setTimeout(() => f.focus({ preventScroll: true }), 30); }
  function hide(...ids) { ids.forEach(id => { const el = $(id); if (el) el.hidden = true; }); }

  // ---------------------------------------------------------------- canvas fitting
  /**
   * Fit a W x H world into the canvas, leaving room for the HUD.
   * Returns { dpr, scale, ox, oy, vw, vh }; call again on resize.
   */
  function fit(canvas, W, H, { top = 96, bottom = 24, side = 12 } = {}) {
    const dpr = Math.min(2, devicePixelRatio || 1), vw = innerWidth, vh = innerHeight;
    canvas.width = Math.round(vw * dpr); canvas.height = Math.round(vh * dpr);
    const scale = Math.max(.1, Math.min((vw - side * 2) / W, (vh - top - bottom) / H));
    return { dpr, scale, vw, vh, ox: (vw - W * scale) / 2, oy: top + (vh - top - bottom - H * scale) / 2 };
  }

  // ---------------------------------------------------------------- small math helpers
  const rand = (a, b) => a + Math.random() * (b - a);
  const randi = (a, b) => Math.floor(rand(a, b + 1));
  const pick = arr => arr[Math.floor(Math.random() * arr.length)];
  const clamp = (v, a, b) => v < a ? a : v > b ? b : v;
  const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  function roundRect(c, x, y, w, h, r) { r = Math.min(r, w / 2, h / 2); c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }

  window.Kit = { $, store, best, initAudio, tone, noise, chord, bindMute, toast, show, hide, fit, rand, randi, pick, clamp, shuffle, roundRect,
    get muted() { return muted; } };
})();
