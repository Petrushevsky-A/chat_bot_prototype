
from ...templates.keyboard import DateKeyboard
from ...templates.viber_serializer import ViberSerializerKeyboard 


class MetaSingletonView(type):
    # Дочернии классы должны учитывать предыдущие свои состояния.
    # Например номер страницы дат
    # Полезно учесть таймаут последнего использования бота, и удалить представление
    _instances = {}
    def __new__(cls, request, *args, **kwargs):
        sender_id = 0
        if cls not in cls._instances:
            cls._instances[request] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]




class DateView(MetaSingletonView):

    def __init__(self, request):
        self.page = 0
        self.response = None

        self._generate_keyboard()
    
    def _generate_keyboard(self):
        serializer_keyboard = ViberSerializerKeyboard(DateKeyboard(page=self.page))
        
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

