from PIL import ImageFont, ImageDraw, Image
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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
                text_ = ""
            else:
                text_ = f"{text_}{i}"
        if len(text_) != 0:
            new_text.append(text_)
        return new_text

    def display(self, text):
        final_text = ""
        data = self.convert_to_array(text)
        datax = data[::-1]
        for x in datax:
            if x in self.punctuation:
                final_text = f"{final_text}{x}"
            else:
                final_text = f"{final_text}{self.reshaper_text(x)}"
        return final_text

    def get_text_width(self, text, font_path, font_size):
        font = ImageFont.truetype(font_path, font_size)
        image = Image.new("RGB", (1000, 100), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        return draw.textlength(text, font=font)

    def ArabicParagraph(self, text, font_name, path, col_width, font_size, align="RIGHT"):
        pdfmetrics.registerFont(TTFont(font_name, path))
        reshaped_text = self.display(text)
        table_data = []
        words = reshaped_text.split(" ")
        current_row_text = ""

        for word in words:
            print(word)
            new_row_text = f"{current_row_text} {word}".strip()
            row_width = self.get_text_width(new_row_text, path, font_size) 

            if row_width > col_width:  
                table_data.append([current_row_text])
                current_row_text = word
            else:
                current_row_text = new_row_text

        if current_row_text: 
            table_data.append([current_row_text.strip()])
        print(current_row_text)

        table = Table(table_data[::-1], colWidths=[col_width], hAlign=align)
        table.setStyle(TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, -1), font_name),
            ('FONTSIZE', (0, 0), (-1, -1), font_size),
        ]))

        return table
