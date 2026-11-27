import sys
from pypdf import PdfReader, PdfWriter
for f in sys.argv[1:]:
    r=PdfReader(f); w=PdfWriter()
    for p in r.pages: w.add_page(p)
    w.add_metadata({'/Title':'Skincare by Dr V · Sephora Prize Europe','/Author':'Dr Vanita Rattan','/Subject':'Corporate, brand and product presentation','/Creator':'Skincare by Dr V','/Producer':'Skincare by Dr V'})
    with open(f,'wb') as o: w.write(o)
