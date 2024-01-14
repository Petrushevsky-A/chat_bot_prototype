
from .button import Button

class Keyboard:
    TYPE = "keyboard" //vk, tg, viber
    BUTTONS = []
    
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
    def __init__(self, type_bot):
        self.buttons = [
            [previous_dates_page, current_dates_page, next_dates_page],
            [monday, tuesday, wednesday, thursday, friday, saturday, sunday],
            [current_day, ],
        ]
{
    "Type": "keyboard",
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "Text": "ФОП Готько",
                "TextOpacity" : "0",
                "BgMedia" : "https://i.ibb.co/7rzVkgc/gotko.jpg",
        "TextHAlign": "left",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "ФОП Готько"
    }, {
    "Columns": 6,
    "Rows": 1,
    "Text": "Полина",
            "TextOpacity" : "0",
            "BgMedia" : "https://i.ibb.co/7rsb6Pc/polina.jpg",
    "TextHAlign": "left",
    "TextVAlign": "middle",
    "ActionType": "reply",
    "ActionBody": "Полина"
    },{
            "Columns": 6,
    "Rows": 1,
    "Text": "JUST Jewellery",
            "TextOpacity" : "0",
            "BgMedia" : "https://i.ibb.co/5TqmnBc/just.jpg",
    "TextHAlign": "left",
    "TextVAlign": "middle",
    "ActionType": "reply",
            "ActionBody": "JUST Jewellery"
    },{
            "Columns": 6,
    "Rows": 1,
    "Text": "Silverado",
            "TextOpacity" : "0",
            "BgMedia" : "https://i.ibb.co/fGpcMSJ/silverado.jpg",
    "TextHAlign": "left",
    "TextVAlign": "middle",
    "ActionType": "reply",
    "ActionBody": "Silverado"
    },{
            "Columns": 6,
    "Rows": 1,
    "Text": "Poli",
            "TextOpacity" : "0",
            "BgMedia" : "https://i.ibb.co/WttKpyw/poli.jpg",
    "TextHAlign": "left",
    "TextVAlign": "middle",
    "ActionType": "reply",
    "ActionBody": "Poli"
    }, {
            "Columns": 6,
    "Rows": 1,
    "Text": "Цепочки",
            "TextOpacity" : "0",
            "BgMedia" : "https://i.ibb.co/GWcfB3r/cepochki.jpg",
    "TextHAlign": "left",
    "TextVAlign": "middle",
    "ActionType": "reply",
    "ActionBody": "Цепочки"
    }, {
            "Columns": 6,
    "Rows": 1,
    "Text": "Вернутся на главное меню",
            "TextOpacity" : "0",
            "BgMedia" : "https://i.ibb.co/CvGsX1t/message.jpg",
    "TextHAlign": "left",
    "TextVAlign": "middle",
    "ActionType": "reply",
    "ActionBody": "Вернутся на главное меню"
    }]
}
