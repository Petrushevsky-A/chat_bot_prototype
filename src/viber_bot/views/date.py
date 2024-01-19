from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage

from ...templates.keyboard import DateKeyboard
from ...templates.viber_serializer import ViberSerializerKeyboard 



class DateView:

    def __init__(self, request):
        self.request=request
        self.page = 0
        self.response = None
        self._generate_keyboard()
    
    def _generate_keyboard(self):
        serializer_keyboard = ViberSerializerKeyboard(DateKeyboard(page=self.page))
        print(f'======= {self.page=}=========')
        self.response = RichMediaMessage(
            rich_media=serializer_keyboard.data 
        )
    
    def _get_page(self):
        self.page = int(self.request.message.text.split()[-1])
        return self.page

    def next_page(self):
        self._get_page()
        self._generate_keyboard()
        return self 

    def previous_page(self):
        self._get_page()
        self._generate_keyboard()
        return self

    def zero_page(self):
        self.page = 0
        return self

