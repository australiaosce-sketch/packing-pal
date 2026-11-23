"""Skincare by Dr V - Black Friday Instagram Stories (1080x1920).
Palette and fonts copied from /Brand/Skills/Instagram Carousels/brand-template/drv_brand.py v1.0.
Colours are only ever used through the names below; check() refuses anything off-palette."""
import os, re, json, subprocess, sys
ESPRESSO='#4B2E20'; COCOA='#321509'; IVORY='#FFFAF7'; BLUSH='#F5DBCE'; CARAMEL='#C8925A'
GOLD='#C9A97E'; ROSE='#C9A08E'; COPPER='#B4703F'; GLOW='#F6CB52'; TRUSTPILOT='#00B67A'
PALETTE=[ESPRESSO,COCOA,IVORY,BLUSH,CARAMEL,GOLD,ROSE,COPPER,GLOW,TRUSTPILOT]
def rgba(h,a):
    assert h in PALETTE; h=h[1:]; return f'rgba({int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)},{a})'
FONTS_CSS="""@font-face{font-family:'Inter Tight';font-weight:800;src:url(https://fonts.gstatic.com/s/intertight/v9/NGSnv5HMAFg6IuGlBNMjxJEL2VmU3NS7Z2mjjwiqXA.ttf) format('truetype')}
@font-face{font-family:'Mulish';font-weight:400;src:url(https://fonts.gstatic.com/s/mulish/v18/1Ptyg83HX_SGhgqO0yLcmjzUAuWexZNRwaA.ttf) format('truetype')}
@font-face{font-family:'Mulish';font-weight:600;src:url(https://fonts.gstatic.com/s/mulish/v18/1Ptyg83HX_SGhgqO0yLcmjzUAuWexU1WwaA.ttf) format('truetype')}
@font-face{font-family:'Mulish';font-weight:800;src:url(https://fonts.gstatic.com/s/mulish/v18/1Ptyg83HX_SGhgqO0yLcmjzUAuWexRNWwaA.ttf) format('truetype')}"""
W,H=1080,1920
TOP=270          # clears the Stories progress bar + profile row
LEFT,RIGHT=80,120
FOOT_Y=1600      # footer sits above the reply bar

CSS=f"""<style>{FONTS_CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{ESPRESSO}}}
.s{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Mulish'}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.k{{font-family:'Mulish';font-weight:800;font-size:30px;letter-spacing:7px;text-transform:uppercase}}
.h{{font-family:'Inter Tight';font-weight:800;line-height:1.0;letter-spacing:-1.5px}}
.b{{font-family:'Mulish';font-weight:600;font-size:40px;line-height:1.3}}
.pill{{display:inline-block;font-family:'Mulish';font-weight:800;font-size:30px;letter-spacing:5px;padding:20px 36px;border-radius:999px;background:{GLOW};color:{COCOA}}}
.foot{{position:absolute;left:{LEFT}px;top:{FOOT_Y}px;font-family:'Mulish';font-weight:800;font-size:24px;letter-spacing:6px}}
</style>"""

def page(inner, dark, last=False):
    fc = IVORY if dark else COCOA
    foot = 'SHOP AT SKINCAREBYDRV.COM' if last else 'SKINCARE BY DR V'
    return f'<!doctype html><html><head><meta charset="utf-8">{CSS}</head><body><div class="s">{inner}<div class="foot" style="color:{fc}">{foot}</div></div></body></html>'

def photo(p): return f'<img class="ph" src="img/{p}">'
def dark_top(h=1000): return f'<div style="position:absolute;left:0;right:0;top:0;height:{h}px;background:linear-gradient(180deg,{rgba(ESPRESSO,.95)} 0%,{rgba(ESPRESSO,.9)} 62%,{rgba(ESPRESSO,0)} 100%)"></div>'
def light_top(h=1000): return f'<div style="position:absolute;left:0;right:0;top:0;height:{h}px;background:linear-gradient(180deg,{rgba(IVORY,.97)} 0%,{rgba(IVORY,.92)} 62%,{rgba(IVORY,0)} 100%)"></div>'
def foot_band(dark): 
    c = ESPRESSO if dark else IVORY
    return f'<div style="position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(0deg,{rgba(c,.7)} 0%,{rgba(c,0)} 100%)"></div>'

def text_block(kicker, head, body, dark, size=96, pill=None, top=TOP):
    kc = GOLD if dark else CARAMEL; hc = IVORY if dark else ESPRESSO; bc = BLUSH if dark else COCOA
    p = f'<div style="margin-top:38px"><span class="pill">{pill}</span></div>' if pill else ''
    b = f'<div class="b" style="color:{bc};margin-top:26px">{body}</div>' if body else ''
    return (f'<div style="position:absolute;left:{LEFT}px;right:{RIGHT}px;top:{top}px">'
            f'<div class="k" style="color:{kc}">{kicker}</div>'
            f'<div class="h" style="color:{hc};font-size:{size}px;margin-top:24px">{head}</div>{b}{p}</div>')

DATES = 'Black Friday, 23rd to 30th November.'
def product(img, dark, kicker, name, tagline, size=92):
    return page(photo(img) + (dark_top() if dark else light_top()) + foot_band(dark) +
                text_block(kicker, f'30% off<br>{name}.', f'{tagline}<br>{DATES}', dark, size=size), dark)

stories = [
  # 1 cover
  page(photo('hairoil.jpg') + dark_top(1000) + foot_band(True) +
       text_block('Black Friday · Now on', '30% off our<br>hair and body<br>routines.',
                  '23rd to 30th November.', True, size=104, pill='BLACK FRIDAY · 30% OFF'), True),
  product('hairtonic.jpg', True, 'Hair · Black Friday', 'Anagen Boost', 'For thinning and brittle hair. Use it every day.'),
  product('shampoo.jpg', False, 'Hair · Black Friday', 'Thickening<br>Shampoo', 'For thinning and brittle hair.', size=88),
  product('bodyexfoliator.jpg', False, 'Body · Black Friday', 'Body Smoothing<br>Exfoliator', 'For skin of colour.', size=84),
  product('bodyoil.jpg', True, 'Body · Black Friday', 'Body Brightening<br>Oil', 'Helps with scars and stretch marks on skin of colour.', size=84),
  product('exfoliatetoglow.jpg', True, 'Glow · Black Friday', 'Exfoliate<br>to Glow', 'For skin of colour.'),
  product('pregnancy.jpg', True, 'Pregnancy · Black Friday', 'Pregnancy<br>Stretch Mark Cream', 'For skin of colour.', size=80),
]
# 8 end card: espresso with full list
items = ['Anagen Boost Hair Tonic','Thickening Shampoo','Strand Strengthening Oil','Scalp Rebalancing Exfoliator',
         'Body Brightening Oil','Deep Cleansing Body Wash','Body Smoothing Exfoliator','Exfoliate to Glow','Pregnancy Stretch Mark Cream']
li = ''.join(f'<div style="display:flex;align-items:center;gap:22px;margin:16px 0"><span style="width:16px;height:16px;border-radius:50%;background:{GLOW};flex:none"></span>'
             f'<span class="b" style="color:{IVORY};font-size:36px">{x}</span></div>' for x in items)
end = (f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 80% 10%,{rgba(COPPER,.35)} 0,{rgba(COPPER,0)} 55%),{ESPRESSO}"></div>'
       + text_block('Black Friday · 23rd to 30th Nov', '30% off all 9.', None, True, size=110)
       + f'<div style="position:absolute;left:{LEFT}px;right:{RIGHT}px;top:560px">{li}</div>'
       + f'<div style="position:absolute;left:{LEFT}px;right:{RIGHT}px;top:1150px">'
         f'<div class="b" style="color:{BLUSH};font-size:36px">Free shipping on minimum spend.</div>'
         f'<div style="margin-top:44px;height:150px;border:4px dashed {rgba(GOLD,.7)};border-radius:28px;display:flex;align-items:center;justify-content:center" class="k"><span style="color:{GOLD}">Link sticker here</span></div></div>'
       + f'<div style="position:absolute;right:{RIGHT}px;top:{FOOT_Y-6}px" class="k"><span style="color:{GOLD};font-size:24px">Love Dr V x</span></div>')
stories.append(page(end, True, last=True))

BANNED=[r'\blighten',r'lightening',r'whiten',r'white skin',r'caucasian',r'\b4\.6\b',r'35,000',r'90\+ countries',r'80,000',r'100k',
        r'15% L-ascorbic',r'oiling (is|isn.t) bad',r'link in bio',r'\bcode\b',r'Super Hydrating Toner']
def check(slides):
    probs=[]; allowed={p.upper() for p in PALETTE}
    for i,h in enumerate(slides,1):
        body=h.replace(FONTS_CSS,'')
        for c in re.findall(r'#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b',body):
            if c.upper() not in allowed: probs.append(f'story {i}: colour {c} not in palette')
        for c in re.findall(r'rgba?\(([^)]*)\)',body):
            n=[x.strip() for x in c.split(',')][:3]; hx='#'+''.join(f'{int(float(v)):02X}' for v in n)
            if hx not in allowed: probs.append(f'story {i}: rgba({c}) not a brand colour')
        if re.search(r'(color|background|fill|stroke)\s*:\s*(black|white|grey|gray|pink|red|blue|green)\b',body): probs.append(f'story {i}: named colour')
        for f in re.findall(r"font-family:\s*'?([A-Za-z ]+?)'?\s*[;}]",body):
            if f not in ('Inter Tight','Mulish'): probs.append(f'story {i}: font {f}')
        text=re.sub(r'<[^>]+>',' ',re.sub(r'<style>.*?</style>','',body,flags=re.S))
        for b in BANNED:
            if re.search(b,text,re.I): probs.append(f'story {i}: banned wording /{b}/')
        if 'class="foot"' not in body: probs.append(f'story {i}: no footer')
        if 'class="k"' not in body: probs.append(f'story {i}: no kicker')
    if 'SHOP AT SKINCAREBYDRV.COM' not in slides[-1]: probs.append('last story must say SHOP AT SKINCAREBYDRV.COM')
    if 'Free shipping on minimum spend' not in slides[-1]: probs.append('last story must say Free shipping on minimum spend')
    return probs

RENDER_JS="""const {chromium}=require('playwright');const jobs=require(process.argv[2]);
(async()=>{const b=await chromium.launch();for(const j of jobs){const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
await p.goto('file://'+j.html,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:j.out,type:'jpeg',quality:92});await p.close();}await b.close();})();"""

if __name__=='__main__':
    wd=os.path.dirname(os.path.abspath(__file__)); probs=check(stories)
    if probs: print('OFF-BRAND, NOT RENDERED:'); [print(' -',p) for p in probs]; sys.exit(1)
    jobs=[]
    for n,h in enumerate(stories,1):
        hp=os.path.join(wd,f'_story_{n:02d}.html'); open(hp,'w').write(h)
        jobs.append({'html':hp,'out':os.path.join(wd,'out',f'DrV_BF_story_{n:02d}.jpg')})
    json.dump(jobs,open(os.path.join(wd,'_jobs.json'),'w')); open(os.path.join(wd,'_render.js'),'w').write(RENDER_JS)
    subprocess.run(['node',os.path.join(wd,'_render.js'),os.path.join(wd,'_jobs.json')],check=True)
    from PIL import Image
    ims=[Image.open(j['out']).resize((270,480)) for j in jobs]
    S=Image.new('RGB',(len(ims)*282+12,504),(255,250,247))
    for i,im in enumerate(ims): S.paste(im,(12+i*282,12))
    S.save(os.path.join(wd,'DrV_BF_stories_preview.jpg'),quality=90)
    print('ON BRAND. Rendered',len(jobs),'stories')
