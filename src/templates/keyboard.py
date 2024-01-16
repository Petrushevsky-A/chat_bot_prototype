from datetime import datetime, timedelta
from dateutil import rrule

from .button import Button

class Keyboard:
    def __init__(self):
        self.buttons = []

    def __add__(self, instance):
        return Keyboard().add_buttons(instance.buttons)
    
    def add_button(self, instance=None):
        if isinstance(instance, Button):
           self.buttons.append(instance) 


    def add_buttons(self, instances=[]):
        print(f'add buttons METHOD  {instances=}')
        if instances and any(
            map(
                lambda instance: isinstance(instance, Button),
                instances
            )
        ):
           self.buttons.append(instances) 

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
    STEP_PAGINATION = 18

    def __init__(self, type_bot=None, page: int =None):
        super().__init__()
        self.create_buttons_paginations()
        # self.create_buttons_name_days()

        self.page = page
        self.create_buttons_days()

        

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
        ])
    
    def create_buttons_days(self):
        #paginate
        
        if isinstance(self.page, int) and not self.page == 0:
            step = self.STEP_PAGINATION*self.page
        else:
            step = 0

        # 6 col *5 row = 30 button max
        # date start for generate button
        start_date = datetime.now()+timedelta(days=step)
        range_date = rrule.rrule(rrule.DAILY,
                                 count=18,
                                 dtstart=start_date)
        buttons_day = []
        russian_name_month = {
            'Jan':'января',
            'Feb':'февраля',
            'Mar':'марта',
            'Apr':'апреля',
            'May':'мая',
            'Jun':'июня',
            'Jul':'июля',
            'Aug':'августа',
            'Sep':'сентября',
            'Oct':'октября',
            'Nov':'ноября',
            'Dec':'декабря'
        }   
        for date in range_date:
            buttons_day.append(
                Button(
                    text=f'''{date.strftime('%d')}
                    {russian_name_month.get(date.strftime('%b'), '')}'''
                )
            )
            if len(buttons_day)==6:
                self.add_buttons(buttons_day)
                buttons_day = []
    

    def get_rows(self):
        return len(self.buttons)

    def get_columns_in_row(self, row_buttons):
        return len(row_buttons)
    
    def __repr__(self):
        pass
