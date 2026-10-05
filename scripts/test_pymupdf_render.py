import fitz
from pathlib import Path

pdfs = list(Path('C:/Users/krist/Desktop/zotero/learning-corpus').rglob('*.pdf'))[:3]
print('PDFs found:', len(pdfs))
for p in pdfs:
    doc = fitz.open(p)
    page = doc[0]
    pix = page.get_pixmap(dpi=150)
    out = Path('C:/Users/krist/AppData/Local/Temp') / f'{p.stem}_page1.png'
    pix.save(out)
    print(f'Rendered: {out} ({out.stat().st_size} bytes)')
    doc.close()
