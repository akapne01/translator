import os

from PyPDF2 import PdfFileReader
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate

from translate_pdfs.fonts import *

"""
This script uses Google Translate library to translate the PDF
"""

"""
Constants
"""
URL_COM = 'translate.google.com'
URL_LV = 'translate.google.lv'
LANG = "lv"

"""
FUNCTIONS
"""


def get_translated_page_content(reader, lang):
    """
    Reads page content from the reader, translates it,
    cleans it and returns page content as a list of strings.
    Each entry in list represents a page
    """
    num_pages = reader.numPages
    page_contents = []
    translator = Translator(service_urls=[URL_COM, URL_LV])
    for p in range(num_pages):
        page = reader.getPage(p)
        translation = translator.translate(page.extractText(), dest=lang)
        result_text = translation.text.replace("\n", " ").replace("W", "")
        page_contents.append(result_text)
    return page_contents


def translate_pdf(path, lang):
    file = open(path, 'rb')
    reader = PdfFileReader(file)
    page_contents = get_translated_page_content(reader, lang)
    
    page_text = []
    name = f'{LANG}_{path}'
    pdf = SimpleDocTemplate(name, pagesize=letter)
    
    for text in page_contents:
        page_text.append(
            Paragraph(text, encoding='utf-8', style=regular))
    
    pdf.build(page_text)


if __name__ == '__main__':
    os.getcwd()
    translate_pdf("example.pdf", LANG)
