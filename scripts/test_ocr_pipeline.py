import fitz
from pathlib import Path
import subprocess
import json

pdfs = list(Path('C:/Users/krist/Desktop/zotero/learning-corpus').rglob('*.pdf'))[:3]
out_dir = Path('C:/Users/krist/AppData/Local/Temp/ocr-test')
out_dir.mkdir(exist_ok=True)
tesseract = Path('C:/Program Files/Tesseract-OCR/tesseract.exe')

results = []
for pdf in pdfs:
    doc = fitz.open(pdf)
    page = doc[0]
    pix = page.get_pixmap(dpi=200)
    img = out_dir / f'{pdf.stem}_page1.png'
    pix.save(img)
    doc.close()

    txt = out_dir / f'{pdf.stem}_page1'
    res = subprocess.run(
        [str(tesseract), str(img), str(txt), '--psm', '6', 'txt'],
        capture_output=True, text=True
    )
    text = (txt.with_suffix('.txt')).read_text(errors='ignore') if txt.with_suffix('.txt').exists() else ''
    results.append({
        'pdf': pdf.name,
        'image': str(img),
        'text': text[:800],
        'returncode': res.returncode,
        'stderr': res.stderr[:300]
    })

print(json.dumps(results, indent=2))
