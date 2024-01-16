
from .views.date import DateView

class Router:
    
    ROUTERS = {
        '>': (DateView, 'next_page'),
        '<': (DateView, 'previous_page'),
        'date':'',
        'add_time_session':'',
        'del_time_session':'',
        'change_time_session':'',
    }

    def __init__(self, request):
        message = request.message.text

        print('=====ROUTER========')
        print(f'{dir(request)=}')
        print(f'{message=}') 
        self.response = self.ROUTERS[message](request)


