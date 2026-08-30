from pathlib import Path
import subprocess, json, os
from concurrent.futures import ThreadPoolExecutor, as_completed

corpus_root = Path(r'C:\Users\krist\Desktop\zotero\learning-corpus')
text_root = corpus_root / '.text'
text_root.mkdir(exist_ok=True)

# Find all PDFs
pdfs = list(corpus_root.glob('**/*.pdf')) + list(corpus_root.glob('**/*.PDF'))
print(f'Found {len(pdfs)} PDFs')

# pdftotext command
def extract_text(pdf_path):
    txt_name = pdf_path.stem + '.txt'
    txt_path = text_root / txt_name
    if txt_path.exists() and txt_path.stat().st_size > 1000:
        return ('skip', pdf_path, txt_path)
    
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', str(pdf_path), str(txt_path)],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0 and txt_path.exists():
            size = txt_path.stat().st_size
            return ('ok', pdf_path, txt_path, size)
        else:
            return ('fail', pdf_path, result.stderr[:200])
    except subprocess.TimeoutExpired:
        return ('timeout', pdf_path, '')
    except Exception as e:
        return ('error', pdf_path, str(e)[:200])

# Process in batches to avoid overwhelming the system
batch_size = 20
results = {'ok': 0, 'skip': 0, 'fail': 0, 'timeout': 0, 'error': 0}

for i in range(0, len(pdfs), batch_size):
    batch = pdfs[i:i+batch_size]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(extract_text, pdf): pdf for pdf in batch}
        for future in as_completed(futures):
            res = future.result()
            status = res[0]
            results[status] = results.get(status, 0) + 1
            
            if status == 'ok':
                pdf_path, txt_path, size = res[1], res[2], res[3]
                print(f'[OK] {pdf_path.name} -> {size:,} bytes')
            elif status == 'skip':
                pdf_path, txt_path = res[1], res[2]
                size = txt_path.stat().st_size
                print(f'[SKIP] {pdf_path.name} -> {size:,} bytes')
            elif status == 'fail':
                pdf_path, err = res[1], res[2]
                print(f'[FAIL] {pdf_path.name}: {err}')
            elif status == 'timeout':
                pdf_path = res[1]
                print(f'[TIMEOUT] {pdf_path.name}')
            else:
                pdf_path, err = res[1], res[2]
                print(f'[ERROR] {pdf_path.name}: {err}')

print(f'\n=== SUMMARY ===')
for k, v in results.items():
    print(f'{k}: {v}')
print(f'Total processed: {sum(results.values())}')
