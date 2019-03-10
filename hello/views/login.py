from django.shortcuts import render, redirect

from hello.models import User


def login_decorator(func):
    def _decorated(request, *args, **kwargs):
        # если человек заходит на защещенные страницы, то нужно проверить куку и что-то сделать
        if func.__name__ == 'login' or func.__name__ == 'registration':
            # если кука то пусть идет на свой профиль, если нет то пусть идет на свою страницу
            if check_user_cookie(request):
                redirect('profile')
            return func(request, *args, **kwargs)
        else:
            # если кука то пусть идет  хочет, если нет то пусть идет на страницу login
            if check_user_cookie(request):
                return func(request, *args, **kwargs)
            redirect('login')
    return _decorated


def check_user_cookie(requst):

    pass


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


@login_decorator
def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        pass


@login_decorator
def registration(request):
    if request.method == 'GET':
        return render(request, "registration.html")
    elif request.method == 'POST':
        name, psw = request.POST['username'], request.POST['psw']
        if get_or_none(User, name=name):
            # такой mail уже есть
            return render(request, "registration.html")
        # если такой email уже есть в базе сказать об этом
        # иначе отправить письмо с ссылкой

@login_decorator
def profile(request):
    if request.method == 'GET':
        return render(request, "profile.html")



