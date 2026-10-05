@echo off
setlocal

echo [tesseract-install] Downloading Tesseract 5.4.0...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe' -OutFile '%TEMP%\tesseract-ocr-setup.exe'"

echo [tesseract-install] Running installer silently...
start /wait "" "%TEMP%\tesseract-ocr-setup.exe" /S /D=C:\Program Files\Tesseract-OCR

echo [tesseract-install] Cleaning up...
del /f "%TEMP%\tesseract-ocr-setup.exe"

echo [tesseract-install] Adding to PATH...
setx /M PATH "%PATH%;C:\Program Files\Tesseract-OCR"

echo [tesseract-install] Done.
pause
