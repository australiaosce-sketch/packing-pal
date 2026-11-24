"""Square (1080x1080) carousel version of the Dr V Black Friday stories, for a YouTube / feed image post.
Uses the palette, fonts and brand check from build_stories.py (copied from brand-template/drv_brand.py)."""
import sys, os, json, subprocess
sys.argv = [sys.argv[0], 'ig']
import build_stories as B
from build_stories import ESPRESSO, COCOA, IVORY, BLUSH, CARAMEL, GOLD, GLOW, COPPER, rgba
S = 1080; PW = 608          # photo panel = exact 9:16 width at 1080 high, so the whole photo shows
TW = S - PW                 # text panel
CSS = B.CSS.replace('width:1080px;height:1920px', f'width:{S}px;height:{S}px')

def page(inner, dark, last=False):
    fc = IVORY if dark else COCOA
    foot = 'SHOP AT SKINCAREBYDRV.COM' if last else 'SKINCARE BY DR V'
    return (f'<!doctype html><html><head><meta charset="utf-8">{CSS}</head><body><div class="s">{inner}'
            f'<div class="foot" style="color:{fc};top:auto;bottom:56px;left:64px;font-size:20px;letter-spacing:5px">{foot}</div></div></body></html>')

def split(img, dark, kicker, head, body, size=64, pill=None, pos='50% 50%'):
    bg = ESPRESSO if dark else IVORY
    kc = GOLD if dark else CARAMEL; hc = IVORY if dark else ESPRESSO; bc = BLUSH if dark else COCOA
    p = f'<div style="margin-top:34px"><span class="pill" style="font-size:22px;letter-spacing:4px;padding:16px 26px;white-space:nowrap">{pill}</span></div>' if pill else ''
    return page(f'<div style="position:absolute;inset:0;background:{bg}"></div>'
                f'<img src="img/{img}" style="position:absolute;right:0;top:0;width:{PW}px;height:{S}px;object-fit:cover;object-position:{pos}">'
                f'<div style="position:absolute;left:64px;width:{TW-104}px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
                f'<div class="k" style="color:{kc};font-size:22px;letter-spacing:5px">{kicker}</div>'
                f'<div class="h" style="color:{hc};font-size:{size}px;margin-top:22px;letter-spacing:-1px">{head}</div>'
                f'<div class="b" style="color:{bc};font-size:28px;margin-top:24px">{body}</div>{p}</div>', dark)

D = 'Black Friday,<br>23rd to 30th November.'
slides = [
  split('hairoil.jpg', True, 'Now on', '30% off our hair and body routines.', '23rd to 30th November.', size=66, pill='BLACK FRIDAY · 30% OFF'),
  split('hairtonic.jpg', True, 'Hair', '30% off Anagen Boost.', f'For thinning and brittle hair. Use it every day.<br><br>{D}'),
  split('shampoo.jpg', False, 'Hair', '30% off Thickening Shampoo.', f'For thinning and brittle hair.<br><br>{D}'),
  split('bodyexfoliator.jpg', False, 'Body', '30% off Body Smoothing Exfoliator.', f'For skin of colour.<br><br>{D}', size=58),
  split('bodyoil.jpg', True, 'Body', '30% off Body Brightening Oil.', f'Helps with scars and stretch marks on skin of colour.<br><br>{D}', size=60),
  split('exfoliatetoglow.jpg', True, 'Glow', '30% off Exfoliate to Glow.', f'For skin of colour.<br><br>{D}'),
  split('pregnancy.jpg', True, 'Pregnancy', '30% off Pregnancy Stretch Mark Cream.', f'For skin of colour.<br><br>{D}', size=56),
]
items = ['Anagen Boost Hair Tonic','Thickening Shampoo','Strand Strengthening Oil','Scalp Rebalancing Exfoliator','Body Brightening Oil',
         'Deep Cleansing Body Wash','Body Smoothing Exfoliator','Exfoliate to Glow','Pregnancy Stretch Mark Cream']
li = ''.join(f'<div style="display:flex;align-items:center;gap:16px;margin:10px 0"><span style="width:12px;height:12px;border-radius:50%;background:{GLOW};flex:none"></span>'
             f'<span class="b" style="color:{IVORY};font-size:28px">{x}</span></div>' for x in items)
slides.append(page(
    f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 85% 10%,{rgba(COPPER,.35)} 0,{rgba(COPPER,0)} 55%),{ESPRESSO}"></div>'
    f'<div style="position:absolute;left:64px;right:64px;top:90px">'
    f'<div class="k" style="color:{GOLD};font-size:22px;letter-spacing:5px">Black Friday · 23rd to 30th November</div>'
    f'<div class="h" style="color:{IVORY};font-size:84px;margin-top:20px">30% off all 9.</div>'
    f'<div style="margin-top:34px;columns:2;column-gap:40px">{li}</div>'
    f'<div class="b" style="color:{BLUSH};font-size:28px;margin-top:30px">Free shipping on minimum spend.</div>'
    f'<div style="margin-top:30px;display:flex;justify-content:space-between;align-items:center"><span class="pill" style="font-size:22px;letter-spacing:4px;padding:16px 26px">SHOP AT SKINCAREBYDRV.COM</span>'
    f'<span class="k" style="color:{GOLD};font-size:22px">Love Dr V x</span></div></div>', True, last=True))

if __name__ == '__main__':
    probs = B.check(slides)
    if probs: print('OFF-BRAND, NOT RENDERED:'); [print(' -', p) for p in probs]; sys.exit(1)
    wd = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(wd, 'square'); os.makedirs(out, exist_ok=True)
    jobs = []
    for n, h in enumerate(slides, 1):
        hp = os.path.join(wd, f'_sq_{n:02d}.html'); open(hp, 'w').write(h)
        jobs.append({'html': hp, 'out': os.path.join(out, f'DrV_BF_square_{n:02d}.jpg')})
    json.dump(jobs, open(os.path.join(wd, '_jobs.json'), 'w'))
    open(os.path.join(wd, '_render.js'), 'w').write(B.RENDER_JS.replace('height:1920', f'height:{S}'))
    subprocess.run(['node', os.path.join(wd, '_render.js'), os.path.join(wd, '_jobs.json')], check=True)
    from PIL import Image
    ims = [Image.open(j['out']).resize((360, 360)) for j in jobs]
    P = Image.new('RGB', (4*372+12, 2*372+12), (255, 250, 247))
    for i, im in enumerate(ims): P.paste(im, (12+(i % 4)*372, 12+(i//4)*372))
    P.save(os.path.join(out, 'DrV_BF_square_preview.jpg'), quality=90)
    for f in os.listdir(wd):
        if f.startswith('_') and f != '__pycache__': os.remove(os.path.join(wd, f))
    print('ON BRAND. Rendered', len(jobs), 'square slides')
