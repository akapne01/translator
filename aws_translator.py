import boto3
from PyPDF2 import PdfFileReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph

from translate_pdfs.fonts import regular

"""
This script uses AWS Translator to translate the PDF.
Please note to change the region to the one you wish to use.
"""

LANG = "lv"
AWS_REGION = 'eu-west-1'


def get_translated_page_content(reader, lang):
    """
    Reads page content from the reader, translates it,
    cleans it and returns page content as a list of strings.
    Each entry in list represents a page
    """
    num_pages = reader.numPages
    page_contents = []
    translate = boto3.client(service_name='translate',
                             region_name=AWS_REGION,
                             use_ssl=True)

    for p in range(num_pages):
        page = reader.getPage(p)

        result = translate.translate_text(Text=page.extractText(),
                                          SourceLanguageCode="auto",
                                          TargetLanguageCode=lang)
        translation = result.get('TranslatedText')

        result_text = translation.replace("\n", " ").replace("W", "")
        page_contents.append(result_text)
    return page_contents


def translate_pdf(path, lang):
    file = open(path, 'rb')
    reader = PdfFileReader(file)
    page_contents = get_translated_page_content(reader, lang)

    page_text = []
    name = f'AWS_{LANG}_{path}'
    pdf = SimpleDocTemplate(name, pagesize=A4)

    for text in page_contents:
        page_text.append(
            Paragraph(text, encoding='utf-8', style=regular))

    pdf.build(page_text)


if __name__ == '__main__':
    file_name = "example.pdf"
    translate_pdf(file_name, LANG)
