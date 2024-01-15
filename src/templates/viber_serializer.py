
class ViberSerializerKeyboard:
    WIDTH_COLUMNS = 6

    def __init__(self, keyboard):
        self.keyboard = keyboard    
        self.data = {
            'Type': 'keyboard',
            'Buttons': []
        }
    
    def set_buttons_data(self):

        for number_row, row_buttons in enumerate(self.keyboard.BUTTONS, 1):
            columns = int(WIDTH_COLUMNS/len(row_columns))

            for button in row_buttons:
                self.data['Buttons'].append({
                    "Columns": columns,
                    "Rows": number_row,
                    "Text": button.text,
                            "TextOpacity" : "0",
                    "TextHAlign": "left",
                    "TextVAlign": "middle",
                    "ActionType": "reply",
                    "ActionBody": button.text,
                })

    def get_data(self):
       return self.data 

