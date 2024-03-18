from img2table.document import Image
from img2table.ocr import TesseractOCR

#in Linux, use 'source .venv/bin/activate'
#if pip hangs, might be trying to connect to XServer, so use 'Display= pip install <package>'

filepath = 'TableExtraction/Images/Table1.png'

ImageFile = Image(src=filepath, detect_rotation=True)

ocr = TesseractOCR(lang="eng")

ImageFile.to_xlsx('tables.xlsx', ocr=ocr, implicit_rows=False, borderless_tables=False,
                min_confidence = 50)