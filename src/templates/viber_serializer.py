
class ViberSerializerKeyboard:
    WIDTH_COLUMNS = 6

    def __init__(self, keyboard):
        self.keyboard = keyboard    
        self.data = {
            'Type': 'keyboard',
            'Buttons': []
        }
        self.set_buttons_data()

    
    def set_buttons_data(self):
        print('====KEYBOARD BUTTONS ====== SET =====')
        print(f'{self.keyboard.buttons=}')
        for number_row, row_buttons in enumerate(self.keyboard.buttons, 1):
            columns = int(self.WIDTH_COLUMNS/len(row_buttons))
            print('=====ROW BUTTONS====')
            print(f'{row_buttons=}')
            for button in row_buttons:
                self.data['Buttons'].append({
                    "Columns": columns,
                    "Rows": 1,
                    "Text": button.text,
                    "TextHAlign": "middle",
                    "TextVAlign": "middle",
                    "ActionType": "reply",
                    "ActionBody": button.text,
                })
        print('=====SET BUTTONS====')
        print(f'{self.data=}')
        return self

    def get_data(self):
       return self.data 

