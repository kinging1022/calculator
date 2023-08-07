import customtkinter as ctk
from settings import *
import darkdetect
from PIL import Image
from button import Button, ImageButton, NumButton, MathButton, MathImageButton


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color=(WHITE, BLACK))
        ctk.set_appearance_mode('light' if is_dark else 'dark')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        self.title('')

        # layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')

        # data
        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='')
        self.display_num = []
        self.full_operation = []

        # widget
        self.create_widget()

        self.mainloop()

    def create_widget(self):
        # font
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size= OUTPUT_FONT_SIZE)

        # output label
        OutputLabel(self, 0, 'SE', main_font, self.formula_string)  # formula
        OutputLabel(self, 1, 'E', result_font, self.result_string)  # result

        # clear(AC) button
        Button(parent=self,
               text=OPERATORS['clear']['text'],
               func=self.clear,
               col=OPERATORS['clear']['col'],
               row=OPERATORS['clear']['row'],
               font=main_font)

        # percentage (%) button
        Button(parent=self,
               text=OPERATORS['percent']['text'],
               func=self.percent,
               col=OPERATORS['percent']['col'],
               row=OPERATORS['percent']['row'],
               font=main_font,
               )

        # invert button
        invert_image = ctk.CTkImage(
            light_image=Image.open(OPERATORS['invert']['image path']['dark']),
            dark_image=Image.open(OPERATORS['invert']['image path']['light'])
        )

        ImageButton(
            parent=self,
            func=self.invert,
            col=OPERATORS['invert']['col'],
            row=OPERATORS['invert']['row'],
            image=invert_image,
        )

        # num button
        for num, data in NUM_POSITIONS.items():
            NumButton(
                parent=self,
                text=num,
                func=self.num_press,
                font=main_font,
                col=data['col'],
                row=data['row'],
                span=data['span']
            )

        # operator button
        for operator, data in MATH_POSITIONS.items():
            if data['image path']:
                button_image = ctk.CTkImage(
                    light_image=Image.open(data['image path']['light']),
                    dark_image=Image.open(data['image path']['dark']))
                MathImageButton(
                    parent=self,
                    operator=operator,
                    func=self.math_press,
                    col=data['col'],
                    row=data['row'],
                    image=button_image
                )

            else:
                MathButton(
                    parent=self,
                    text=data['character'],
                    operator=operator,
                    func=self.math_press,
                    font=main_font,
                    col=data['col'],
                    row=data['row'],
                )

    def num_press(self, value):
        self.display_num.append(str(value))
        full_number = ''.join(self.display_num)
        self.result_string.set(full_number)

    def math_press(self, value):
        current_number = ''.join(self.display_num)
        if current_number:
            self.full_operation.append(current_number)

            if value != '=':
                # update data
                self.full_operation.append(value)
                self.display_num.clear()
                # update output
                self.result_string.set('')
                self.formula_string.set(''.join(self.full_operation))
            else:
                formula = ''.join(self.full_operation)
                result = eval(formula)

                # format the result
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)

                # update data
                self.full_operation.clear()
                self.display_num = [str(result)]

                # update my output
                self.result_string.set(result)
                self.formula_string.set(formula)

    def invert(self):
        current_number = ''.join(self.display_num)
        if current_number:
            if float(current_number) > 0:
                self.display_num.insert(0, '-')
            else:
                del self.display_num[0]
            self.result_string.set(''.join(self.display_num))

    def clear(self):
        # clear output
        self.formula_string.set('')
        self.result_string.set(0)

        # clear data
        self.display_num.clear()
        self.full_operation.clear()

    def percent(self):
        if self.display_num:

            # get percent number
            current_number = float(''.join(self.display_num))
            percent_number = current_number/100

            # update  data and output
            self.display_num = list(str(percent_number))
            self.result_string.set(''.join(self.display_num))


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(parent,  font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)


Calculator(darkdetect.isDark())
