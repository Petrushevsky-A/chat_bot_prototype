from viberbot.api.messages.keyboard_message import KeyboardMessage

from ...templates.keyboard import DateKeyboard
from ...templates.viber_serializer import ViberSerializerKeyboard 


class View(type):
    # Дочернии классы должны учитывать предыдущие свои состояния.
    # Например номер страницы дат
    # Полезно учесть таймаут последнего использования бота, и удалить представление
    # По сути это слегка переделанный Singleton
    _instances = {}
    def __new__(cls, request, *args, **kwargs):
        sender_id = request.sender.id
        if sender_id not in cls._instances:
            cls._instances[sender_id] = type.__new__(
                cls,'View',(View, ), {'request':request}
            )
            
        return cls._instances[sender_id]


class DateView(View):

    def __init__(self, request):
        self.page = 0
        self.response = None
        self._generate_keyboard()
    
    def _generate_keyboard(self):
        serializer_keyboard = ViberSerializerKeyboard(DateKeyboard(page=self.page))
        print('=====INTSTANCE=====')
        print(f'{self.page=}')
        self.response = KeyboardMessage(
            keyboard=serializer_keyboard.data 
        )

    def next_page(self):
        self.page += 1
        self._generate_keyboard()
        return self 

    def previous_page(self):
        self.page -=1
        self._generate_keyboard()
        return self

