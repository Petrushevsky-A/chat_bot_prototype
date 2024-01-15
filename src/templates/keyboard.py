from typing
from .button import Button

class Keyboard:
    BUTTONS = []: List[List[Button]]
    
    def __add__(self, instance):
        return Keyboard().add_buttons(instance.BUTTONS)

    def add_button(self, instance=None):
        if isinstance(instance, Button):
           self.BUTTONS.append(instance) 


    def add_buttons(self, instances=[]):
        if not instances and any(map(isinstance(instances, Button))):
           self.BUTTONS.extend(instances) 

class ViberDateKeyboard():
    def __init__(self):
        pass    


class TelegramDateKeyboard:
    def __init__(self):
        pass

class VkDateKeyboard:
    def __init__(self):
        pass

class DateKeyboard(Keyboard):
    def __init__(self, type_bot=None):
        self.create_buttons_paginations
        self.create_buttons_name_days
        

    def create_buttons_paginations(self):
        previous_dates_page = Button(text='<')
        current_dates_page = Button(text='Дата')
        next_dates_page = Button(text='>')
        self.add_buttons([
            previous_dates_page,
            current_dates_page,
            next_dates_page,
        ])
    
    def create_buttons_name_days(self):
        monday = Button(text='Пн')
        tuesday = Button(text='Вт')
        wednesday = Button(text='Ср')
        thursday = Button(text='Чт')
        friday  = Button(text='Пт')
        saturday = Button(text='Сб')
        # sunday viber off
        self.add_buttons([
            monday,
            tuesday,
            wednesday,
            thursday,
            friday,
            saturday,
        ],
)

    def get_rows(self):
        return len(self.buttons)

    def get_columns_in_row(self, row_buttons):
        return len(row_buttons)
    
    def __repr__(self):
        pass
