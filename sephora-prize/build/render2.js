const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + __dirname + '/deck2.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const fonts = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight));
  console.log('fonts', [...new Set(fonts)].join(', '));
  const secs = await p.$$('section');
  for (let i = 0; i < secs.length; i++) await secs[i].screenshot({ path: `prev/b${i + 1}.png` });
  const of = await p.evaluate(() => [...document.querySelectorAll('section')].map((s, i) => {
    const sr = s.getBoundingClientRect(); const bad = [];
    s.querySelectorAll('*').forEach(e => {
      const r = e.getBoundingClientRect();
      if (r.height > 0 && r.bottom > sr.bottom - 40 && !['photo', 'foot', 'pg'].some(c => e.classList.contains(c))) bad.push(e.tagName + ':' + (e.textContent || '').trim().slice(0, 30));
    });
    return (i + 1) + ': ' + bad.slice(0, 3).join(' | ');
  }));
  console.log(of.join('\n'));
  await p.pdf({ path: '../Skincare_by_Dr_V_Sephora_Prize_Presentation_v2.pdf', width: '1920px', height: '1080px', printBackground: true });
  await b.close();
})();
