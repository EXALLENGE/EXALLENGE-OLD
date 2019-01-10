from django.http import HttpResponse


def login_decorator(func):
    def _decorated(request, *args, **kwargs):
        if func.__name__ == 'login':
            print(request)
        return func(request, *args, **kwargs)
    return _decorated


@login_decorator
def login(request):
    return HttpResponse('login')

