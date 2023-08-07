from customtkinter import CTkButton
from settings import *


class Button(CTkButton):
    def __init__(self, parent, func, text, col, row, font, span=1, color='dark-gray'):
        super().__init__(parent,
                         text=text,
                         command=func,
                         corner_radius=STYLING['corner-radius'],
                         font=font,
                         fg_color=COLORS[color]['fg'],
                         hover_color=COLORS[color]['hover'],
                         text_color=COLORS[color]['text'],
                         )
        self.grid(column=col, row=row, sticky='nsew', columnspan=span, padx=STYLING['gap'], pady=STYLING['gap'])


class NumButton(Button):
    def __init__(self, parent, func, text, col, row, font, span, color='light-gray'):
        super().__init__(parent=parent,
                         text=text,
                         func=lambda: func(text),
                         font=font,
                         col=col,
                         row=row,
                         color=color,
                         span=span,
                         )


class MathButton(Button):
    def __init__(self, parent, func, text, col, row, font, operator, color='orange'):
        super().__init__(parent=parent,
                         text=text,
                         func=lambda: func(operator),
                         font=font,
                         col=col,
                         row=row,
                         color=color,
                         )


class ImageButton(CTkButton):
    def __init__(self, parent, func,  col, row, image, text='', color='dark-gray'):
        super().__init__(parent,
                         text=text,
                         command=func,
                         corner_radius=STYLING['corner-radius'],
                         image=image,
                         fg_color=COLORS[color]['fg'],
                         hover_color=COLORS[color]['hover'],
                         text_color=COLORS[color]['text'],

                         )
        self.grid(column=col, row=row, sticky='nsew', padx=STYLING['gap'])


class MathImageButton(ImageButton):
    def __init__(self, parent, operator, func, col, row, image, color='orange'):
        super().__init__(
            parent=parent,
            func=lambda: func(operator),
            col=col,
            row=row,
            image=image,
            color=color
        )

        self.grid(column=col, row=row, sticky='nsew', padx=STYLING['gap'])

