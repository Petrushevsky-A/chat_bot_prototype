
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
        print(f'{message=}')

        self.view, *self.methods = self.ROUTERS[message]
        self.view = self.view(request)(request)
        for method in self.methods:
            getattr(self.view, method)()

        self.response = self.view.response 


