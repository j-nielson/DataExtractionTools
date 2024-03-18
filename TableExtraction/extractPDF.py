from img2table.document import PDF
from img2table.ocr import TesseractOCR

#in Linux, use 'source .venv/bin/activate'
#if pip hangs, might be trying to connect to XServer, so use 'Display= pip install <package>'

filepath = 'TableExtraction/PDFs/NielsonBrahney2024_draft.pdf'
# filepath = 'TableExtraction/PDFs/pdf4.pdf'

PDFdoc = PDF(src=filepath, pdf_text_extraction=True, detect_rotation=True)

ocr = TesseractOCR(lang="eng")

# Table identification
# pdf_tables = PDFdoc.extract_tables(ocr=ocr, implicit_rows=True, borderless_tables=True)

# Result of table identification
# print(pdf_tables)

PDFdoc.to_xlsx('tables.xlsx', ocr=ocr, implicit_rows=False, borderless_tables=False,
                min_confidence = 50)