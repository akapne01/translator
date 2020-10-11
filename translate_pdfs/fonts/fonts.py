import os

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

directory = os.getcwd() + "/fonts/"
"""
CONSTANTS
"""
BODY_FONT_SIZE = 12
TITLE_FONT_SIZE = 14
ALIGNMENT_RIGHT = 0
SPACING_BETWEEN_LINES = 20
SPACE_AFTER = 14
FIRST_LINE_INDENT = 12
REGULAR_FONT_NAME = 'NotoSerif-Regular'
BOLD_FONT_NAME = 'NotoSerif-Bold'
ITALIC_FONT_NAME = 'NotoSerif-Italic'
BOLDITALIC_FONT_NAME = 'NotoSerif-BoldItalic'

REGULAR_FONT_FILE = os.path.join(directory, REGULAR_FONT_NAME + ".ttf")
BOLD_FONT_FILE = os.path.join(directory, BOLD_FONT_NAME + ".ttf")
ITALIC_FONT_FILE = os.path.join(directory, ITALIC_FONT_NAME + ".ttf")
BOLDITALIC_FONT_FILE = os.path.join(directory, BOLDITALIC_FONT_NAME + ".ttf")

"""
Registers Custom TTF fonts that are in the fonts directory.
"""
pdfmetrics.registerFont(TTFont('NotoSerif-Regular', REGULAR_FONT_FILE))
pdfmetrics.registerFont(TTFont('NotoSerif-BoldItalic', BOLDITALIC_FONT_FILE))
pdfmetrics.registerFont(TTFont('NotoSerif-Bold', BOLD_FONT_FILE))
pdfmetrics.registerFont(TTFont('NotoSerif-Italic', ITALIC_FONT_FILE))

style = getSampleStyleSheet()


def create_body_font(name):
    """
    Defines a paragraph style for the main text body.
    """
    return ParagraphStyle(name,
                          fontName=name,
                          fontSize=BODY_FONT_SIZE,
                          parent=style['Normal'],
                          alignment=ALIGNMENT_RIGHT,
                          leading=SPACING_BETWEEN_LINES,
                          firstLineIndent=FIRST_LINE_INDENT,
                          spaceAfter=SPACE_AFTER)


def create_title_font(name, style_name):
    """
    Defines a paragraph style for titles
    """
    return ParagraphStyle(name,
                          fontName=name,
                          fontSize=TITLE_FONT_SIZE,
                          parent=style[style_name],
                          alignment=ALIGNMENT_RIGHT,
                          leading=SPACING_BETWEEN_LINES,
                          firstLineIndent=FIRST_LINE_INDENT,
                          spaceAfter=SPACE_AFTER)


"""
Creates various types of fonts that can be imported and used to format PDF files
"""
regular = create_body_font(REGULAR_FONT_NAME)
bold = create_body_font(BOLD_FONT_NAME)
italic = create_body_font(ITALIC_FONT_NAME)
boldItalic = create_body_font(BOLDITALIC_FONT_NAME)
heading1 = create_title_font(BOLD_FONT_NAME, 'Heading1')
heading2 = create_title_font(BOLD_FONT_NAME, 'Heading2')
heading3 = create_title_font(BOLD_FONT_NAME, 'Heading3')
heading4 = create_title_font(BOLD_FONT_NAME, 'Heading4')
heading5 = create_title_font(BOLD_FONT_NAME, 'Heading5')
