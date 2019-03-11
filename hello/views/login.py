from django.shortcuts import render, redirect

from hello.models import User


def check_user_cookie(requst):
    pass


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        name, psw = request.POST['username'], request.POST['psw']
        if get_or_none(User, name=name):
            # поставить куку
            # пустить в профиль
            pass
        return render(request, "login.html", {'message': 'У нас нет такого логина'})


def registration(request):
    if request.method == 'GET':
        return render(request, "registration.html")
    elif request.method == 'POST':
        name, psw = request.POST['username'], request.POST['psw']
        if get_or_none(User, name=name):
            # такой mail уже есть
            return render(request, "registration.html", {'message': 'Пользователь с таким email уже зарегестрирован'})
        # если такой email уже есть в базе сказать об этом
        # иначе отправить письмо с ссылкой
        return render(request, "message.html", {'message': 'У нас нет такого логина'})


def profile(request):
        return render(request, "profile.html")



