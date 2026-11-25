"""Builds artwork.html: one page per product, from products.md / business.md / Shopify (25 Nov 2026)."""
R = 1.195  # ECB 24 Nov 2026
GAP = '<span class="gap">TO ADD</span>'

P = [
 dict(n="Oil Melting Cleanser", size="100ml", gbp=[23], img="omc_s.jpg", range="Complete Daily Range · Step 1 (PM)",
      what="An oil cleanser: the first step of the evening double cleanse.",
      hero=["5% cannabis oil"],
      use=["PM: massage onto dry skin, then follow with Micellar Gel Wash.", "Part of the PM routine: Oil Melting Cleanser, Micellar Gel Wash, Toner, Exfoliate to Glow (weekly), Antioxidant Power Serum, Cera Pep."],
      who=["16+. Normal, dry and combination skin.", "Suitable in pregnancy and breastfeeding.", "Contains cannabis oil, which may block import to some countries (e.g. Singapore)."],
      results=["Range trial (independent, 50 people, 4 weeks): 94% skin more supple, 87% more hydrated, 81% brighter with better texture."],
      gaps=["Full ingredient list (INCI)", "Barcode (EAN)", "Box/bottle dieline and dimensions", "PAO / shelf life"]),
 dict(n="Micellar Gel Wash", size="150ml", gbp=[19], img="mgw_s.jpg", range="Complete Daily Range · Step 2 (AM & PM)",
      what="A gel cleanser for morning and evening, with niacinamide.",
      hero=["2% niacinamide"],
      use=["AM: Micellar Gel Wash, (Vitamin C Glow Serum), Cera Pep, InZincable.", "PM: after Oil Melting Cleanser."],
      who=["Normal, dry and combination skin. Also for children 2+ with normal skin.", "Suitable in pregnancy and breastfeeding."],
      results=["Range trial (independent, 50 people, 4 weeks): 94% skin more supple, 87% more hydrated, 81% brighter with better texture."],
      gaps=["Full ingredient list (INCI)", "Barcode (EAN)", "Dieline and dimensions", "PAO / shelf life"]),
 dict(n="Super Hydrating Toner", size="150ml", gbp=[20], img="sht_s.jpg", range="Complete Daily Range · Step 3 (PM)",
      what="A hydrating toner that preps the skin after cleansing, before exfoliation and serum.",
      hero=[GAP + " Hero ingredients aren't in products.md. Copy them from the product page or the formula sheet"],
      use=["PM: after Micellar Gel Wash, before Exfoliate to Glow / Antioxidant Power Serum.", "Rosacea or sensitive routine: AM after cleansing."],
      who=["Normal, dry and combination skin.", "Suitable in pregnancy and breastfeeding."],
      results=["Range trial (independent, 50 people, 4 weeks): 94% skin more supple, 87% more hydrated, 81% brighter with better texture."],
      gaps=["Hero ingredients and %", "Full ingredient list (INCI)", "Barcode (EAN)", "Dieline and dimensions", "PAO / shelf life"]),
 dict(n="Exfoliate to Glow", size="50ml", gbp=[20], img="etg_s.jpg", range="Complete Daily Range · Step 4 (PM, weekly)",
      what="A once-a-week wash-off exfoliant with two gentle AHAs, for brighter skin and better texture.",
      hero=["5% mandelic acid", "5% lactic acid"],
      use=["Once a week in the evening, after the toner. Wash off.", "Not on the same day as the Facial Pigmentation Kit."],
      who=["Normal, dry and combination skin. Not around the eyes.", "Suitable in pregnancy and breastfeeding.", "Wait 72 hours after laser or professional treatments have healed."],
      results=["81% saw brighter skin and better texture (Daily Range trial, independent, 50 people, 4 weeks)."],
      gaps=["Full ingredient list (INCI)", "Barcode (EAN)", "Dieline and dimensions", "PAO / shelf life"]),
 dict(n="Antioxidant Power Serum", size="30ml", gbp=[48], img="aps_s.jpg", range="Complete Daily Range · Step 5 (PM)",
      what="A night serum combining three forms of vitamin A with fat-soluble vitamin C and antioxidants, in an airless pump.",
      hero=["0.1% retinaldehyde", "0.1% retinol", "0.2% retinyl palmitate", "0.5% tetrahexyldecyl ascorbate (vitamin C)", "0.5% vitamin E", "Coenzyme Q10"],
      use=["PM after the toner (or after Exfoliate to Glow is washed off), then Cera Pep.", "New to vitamin A: alternate nights first."],
      who=["16+. Not for oily skin.", "Not in pregnancy or breastfeeding.", "Wait 6 months after isotretinoin."],
      results=["Results in 2 to 4 weeks, full results at 12 weeks.", "Pure Beauty Awards 2026: Best Serum (Judges' Choice)."],
      gaps=["Full ingredient list (INCI)", "Barcode (EAN)", "Dieline and dimensions", "PAO / shelf life"]),
 dict(n="Cera Pep Brightening Moisturiser", size="100ml", gbp=[32], img="cp_s.jpg", range="Complete Daily Range · Step 6 (AM & PM)",
      what="A barrier-repairing brightening moisturiser with ceramides, peptides and stem cell technology. Our #2 best seller.",
      hero=["4% glycerin", "2% niacinamide", "25% emollients (shea butter, olive glycerides)", "Ceramides", "Peptides (acetyl hexapeptide-49, palmitoyl tripeptide-8)", "Glycyrrhizic acid (liquorice)", "Panthenol · vitamin E · DermStim"],
      use=["AM after Micellar Gel Wash, then InZincable.", "PM as the last step."],
      who=["16+. Normal, dry and combination skin (oily skin: TRIO gels). Safe around the eyes.", "Suitable in pregnancy. Non-comedogenic.", "Also for children 2+ with normal skin."],
      results=["Results in 2 to 4 weeks, full results at 12 weeks.", "18,907 orders in the last 12 months."],
      gaps=["Full ingredient list (INCI)", "Barcode (EAN)", "Dieline and dimensions", "PAO / shelf life"]),
 dict(n="InZincable SPF50", size="50ml · 120ml", gbp=[28, 53], img="inzincable_s.jpg", img2="inzbox_s.jpg", range="Sun protection · Last step (AM)",
      what="A mineral SPF50 with no white cast on Black and brown skin, protecting against UVA, UVB and blue light. Our #1 best seller.",
      hero=["17% zinc oxide (the only UV filter, no chemical filters)", "PA++++", "MelaShield: stem cell, vitamin and pigment-regulating complex", "Niacinamide", "Capsicum extract (blue light)", "Bisabolol · vitamin E · argan oil"],
      use=["Shake. Last step in the morning: ¼ to ½ teaspoon for the face.", "Reapply every 2 hours outdoors, and after swimming or towel-drying."],
      who=["From age 2. Suitable in pregnancy. Non-comedogenic.", "Not water resistant. Not for the lips.", "Shelf life: 12 months open, best within 6."],
      results=["Consumer trial (2021, 51 people aged 30 to 64, 4 weeks): 82% said it looked invisible, 73% saw improved hyperpigmentation, 88% would recommend it.", "Marie Claire: #1 Mineral Sunscreen for Dark Skin."],
      gaps=["Full ingredient list (INCI)", "Barcode (EAN)", "Dieline and dimensions", "SPF/PA test certificates (for Sephora compliance)"]),
 dict(n="Vitamin C Glow Serum", size="50ml / 1.69 fl oz", gbp=[48], img="vitc_s.jpg", img2="vitc_dieline.jpg", range="Brightening serum · AM",
      what="A morning brightening serum for an even skin tone, built on gentle vitamin C derivatives (no L-ascorbic acid) in an airless pump. Our push product.",
      hero=["2% tetrahexyldecyl ascorbate (fat-soluble vitamin C) · 3-O-ethyl ascorbic acid", "2% niacinamide · 2% peptide complex", "Bakuchiol · coenzyme Q10", "Ceramide complex · liquorice root · glycerin · phytic acid"],
      use=["AM after cleansing, on dry skin, then moisturiser and SPF50.", "Start once a day, build to twice a day."],
      who=["16+. All skin types if the skin isn't damaged or sensitive.", "Suitable in pregnancy and breastfeeding (check with your healthcare professional)."],
      results=["Plumper the next day, brighter at 2 weeks, hyperpigmentation improves at 8 to 12 weeks."],
      known=["Box: paper box for 50ml airless pump, 49.5 × 49.5 × 116 mm", "Barcode (EAN-13): 5061062150558", "Made for: Dr Vanita Rattan, Ace Medicine Ltd, 27 Old Gloucester St, London WC1N 3AX, UK", "Box claims: Fragrance free · No drying alcohols · No essential oils · No witch hazel"],
      gaps=["Full ingredient list (INCI): the box lists key ingredients only", "PAO / shelf life", "EU Responsible Person address on the box (needed for EU sale)"]),
]

def page(i, p):
    eur = " / ".join(f"£{g} (≈ €{g*R:.0f})" for g in p["gbp"])
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    known = f'<div class="box ok"><h4>On the pack (from your box artwork)</h4><ul>{li(p["known"])}</ul></div>' if p.get("known") else ""
    img2 = f'<img class="img2" src="img/{p["img2"]}" alt="">' if p.get("img2") else ""
    return f'''<section class="page">
 <div class="left"><img class="prod" src="img/{p["img"]}" alt="{p["n"]}">{img2}</div>
 <div class="right">
  <div class="kicker">{p["range"]}</div>
  <h2>{p["n"]}</h2>
  <p class="meta">{p["size"]} · {eur} · NAFE safe: no denatured alcohol, fragrance or essential oils</p>
  <p class="what">{p["what"]}</p>
  <div class="cols">
   <div><h4>Hero ingredients</h4><ul>{li(p["hero"])}</ul><h4>How to use</h4><ul>{li(p["use"])}</ul>{known}</div>
   <div><h4>Who it's for</h4><ul>{li(p["who"])}</ul><h4>Results &amp; proof</h4><ul>{li(p["results"])}</ul>
   <div class="box"><h4>Still needed for print / compliance</h4><ul>{li(p["gaps"])}</ul></div></div>
  </div>
 </div>
 <div class="foot">SKINCARE BY DR V · PRODUCT ARTWORK SHEET</div><div class="pg">{i}</div>
</section>'''

cover_tiles = "".join(f'<div class="tile"><img src="img/{p["img"]}" alt=""><b>{p["n"]}</b><span>{p["size"]}</span></div>' for p in P)
html = f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Skincare by Dr V · Product artwork sheet</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700;800&family=Mulish:wght@400;600;800&display=swap" rel="stylesheet">
<style>
:root{{--espresso:#4B2E20;--cocoa:#321509;--ivory:#FFFAF7;--blush:#F5DBCE;--caramel:#C8925A;--gold:#C9A97E;--rose:#C9A08E;--copper:#B4703F;--glow:#F6CB52}}
@page{{size:1920px 1080px;margin:0}} *{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Mulish,sans-serif;color:var(--cocoa);background:var(--ivory);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;background:var(--ivory);display:flex}}
.left{{width:760px;background:var(--blush);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;padding:60px}}
.prod{{width:560px;height:560px;object-fit:contain;mix-blend-mode:multiply}}
.img2{{width:300px;max-height:300px;object-fit:contain;mix-blend-mode:multiply;border-radius:10px}}
.right{{flex:1;padding:62px 110px 100px 90px}}
.kicker{{font-weight:800;font-size:18px;letter-spacing:.26em;text-transform:uppercase;color:var(--caramel);margin-bottom:18px}}
h1,h2{{font-family:"Inter Tight";font-weight:800;letter-spacing:-.02em;color:var(--espresso);line-height:1.02}}
h2{{font-size:66px}} h1{{font-size:96px}}
.meta{{font-size:19px;font-weight:600;color:var(--copper);margin-top:14px}}
.what{{font-size:25px;line-height:1.45;margin-top:22px;max-width:980px}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin-top:18px}}
h4{{font-family:"Inter Tight";font-weight:800;font-size:20px;color:var(--espresso);margin:18px 0 8px;letter-spacing:.02em}}
ul{{padding-left:22px}} li{{font-size:18px;line-height:1.4;margin-bottom:3px}}
.box{{border:2px dashed var(--rose);border-radius:14px;padding:4px 20px 12px;margin-top:20px}}
.box.ok{{border:2px solid var(--gold);background:var(--ivory)}}
.gap{{background:var(--glow);font-weight:800;padding:1px 8px;border-radius:6px;font-size:15px}}
.foot{{position:absolute;right:110px;bottom:44px;font-weight:800;font-size:15px;letter-spacing:.26em;color:var(--caramel)}}
.pg{{position:absolute;left:800px;bottom:44px;font-size:15px;font-weight:600;color:var(--rose)}}
.cover{{flex-direction:column;padding:100px 120px;background:var(--espresso)}}
.cover h1{{color:var(--ivory)}} .cover .kicker{{color:var(--gold)}}
.cover p{{color:var(--blush);font-size:25px;line-height:1.45;max-width:1300px;margin-top:20px}}
.tiles{{display:grid;grid-template-columns:repeat(8,1fr);gap:16px;margin-top:56px}}
.tile{{background:var(--ivory);border-radius:16px;padding:14px;display:flex;flex-direction:column;gap:6px}}
.tile img{{width:100%;aspect-ratio:1;object-fit:contain;mix-blend-mode:multiply}}
.tile b{{font-family:"Inter Tight";font-size:18px;color:var(--espresso);line-height:1.15}} .tile span{{font-size:15px;color:var(--copper)}}
</style></head><body>
<section class="page cover">
 <div class="kicker">Skincare by Dr V · Product artwork sheet · Draft 1 · 25 Nov 2026</div>
 <h1>The Complete Daily Range,<br>InZincable SPF50 &amp; Vitamin C Glow Serum</h1>
 <p>One page per product: real pack photo, size, price, hero ingredients, how to use, who it's for and approved results. Built from products.md, business.md, Shopify and your Vitamin C box artwork. Anything not in those files is listed under “Still needed” instead of guessed.</p>
 <div class="tiles">{cover_tiles}</div>
 <p style="font-size:18px;color:var(--gold);margin-top:34px">Not print-ready: final box and label artwork needs the printer's dielines, the full INCI lists and the barcodes for each pack. Euro prices at the ECB rate of 24 Nov 2026 (£1 ≈ €1.195).</p>
</section>
{"".join(page(i+2, p) for i, p in enumerate(P))}
</body></html>'''
open("artwork.html", "w").write(html)
print("pages", len(P) + 1)
