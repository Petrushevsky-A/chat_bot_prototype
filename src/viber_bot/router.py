
from .views.date import DateView

class Router:
    
    ROUTERS = {
        '>': (DateView, 'next_page'),
        '<': (DateView, 'previous_page'),
        'Дата':(DateView, 'zero_page'),
        'add_time_session':'',
        'del_time_session':'',
        'change_time_session':'',
    }

    def __init__(self, request):
        route, *params = request.message.text.split()

        self.view, *self.methods = self.ROUTERS[route]
        print(f'==={self.view=}')
        self.view = self.view(request)
        for method in self.methods:
            getattr(self.view, method)()

        self.response = self.view.response 


