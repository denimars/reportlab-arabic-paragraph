from arabic_reshaper import reshape
from bidi.algorithm import get_display
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors



class ArabicParagraph:
    def __init__(self):
        self.punctuation = [".", ",", "?", "!", ":", ";", "\"", "'", "/", "(", ")", "[", "]", ".", "-", "—", "<", ">", "%", "$", "*", "^", "="]

    def reshaper_text(self, text):
        return get_display(reshape(text))
    
    def convert_to_array(self, text):
        new_text = []
        text_ = ""
        for i in text:
            if i in self.punctuation:
                new_text.append(text_)
                new_text.append(i)
                text_ =""
            else:
                text_ = "{}{}".format(text_, i)
        if len(text_)!=0:
            new_text.append(text_)
        return new_text

    def display(self, text):
        final_text = ""
        data = self.convert_to_array(text)
        datax = data[::-1]
        for x in datax:
            if x in self.punctuation:
                final_text = "{}{}".format(final_text, x)
            else:
                final_text = "{}{}".format(final_text, self.reshaper_text(x))
        # print(final_text)
        return final_text
    
    def ArabicParagraph(self, text, font_name, path, col_width, font_size, align="RIGHT"):
        pdfmetrics.registerFont(TTFont(font_name, path))
        arabic_text = self.display(text)
        # text_arabic_width = stringWidth(arabic_text, font_name, font_size)
        table_data=[]
        text_ = arabic_text.replace("\n","")
        words = text_.split(" ")
        print(words)
        curren_row_text = ""
        for word in words:
            new_row_text = curren_row_text + " "+word if curren_row_text else word
            row_width = stringWidth(new_row_text, font_name, font_size)
            if row_width >col_width:
                table_data.append([curren_row_text])
                curren_row_text = word
            else:
                curren_row_text = new_row_text
        if curren_row_text:
            table_data.append([curren_row_text])
        # print(table_data)
        table = Table(table_data[::-1], colWidths=[col_width], hAlign=align)
        table.setStyle(TableStyle([
            # ('BACKGROUND', (0, 0), (-1, -1), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, -1), 'amiri'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            # ('BOX', (0, 0), (-1, -1), 1, colors.black),
            # ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        return table


