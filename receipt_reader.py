from PIL import Image
import pytesseract

# Googled a bit and found Tesseract, an OCR library mad by google that seem to be recommended by some so here is a test of this
# This is just a test script based on the  to check if it works ok,


# List of available languages
print("\nAvailable languages : {}".format( pytesseract.get_languages(config='')))

# Simple image to string
print(pytesseract.image_to_string(Image.open('test.png'), lang='nor'))

# Get a searchable PDF 
# This one is pretty cool, you can use serach for words in the pdf, and a bounding box shows the hits
pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default


# Some other functions that might be useful.
# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.png')))

# # Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

# # Get ALTO XML output
# xml = pytesseract.image_to_alto_xml('test.png')

print("Finnished")