import random
import string

from passlib.hash import pbkdf2_sha256
from django.shortcuts import render

from hello.models import User
from hello.utils.send_email import send_email


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def login(request):
    if get_or_none(User, logged_in_cookie=request.COOKIES.get('logged_in_cookie')):
        return render(request, "profile.html")
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        login_for_log, psw = request.POST['login'], request.POST['psw']
        if get_or_none(User, login=login_for_log, psw=psw):
            # поставить куку
            # пустить в профиль
            return render(request, "profile.html")
        return render(request, "login.html", {'message': 'У нас нет такого логина'})


def registration(request):
    if get_or_none(User, logged_in_cookie=request.COOKIES.get('logged_in_cookie')):
        return render(request, "profile.html")
    if request.method == 'GET':
        return render(request, "registration.html")
    elif request.method == 'POST':
        login_for_reg, psw = request.POST['login'], request.POST['psw']
        hash_psw = pbkdf2_sha256.encrypt(psw, rounds=200000, salt_size=16)
        if get_or_none(User, login=login_for_reg):
            # такой mail уже есть
            return render(request, "registration.html", {'message': 'Пользователь с таким email уже зарегестрирован'})
        # если такой email уже есть в базе сказать об этом
        # иначе отправить письмо с ссылкой
        unique_url = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
        User.objects.create(login=login_for_reg, psw=hash_psw, tmp_url=unique_url)
        send_email(login_for_reg, f'http://127.0.0.1:8000/check/{unique_url}')
        return render(request, "message.html", {'message': 'Мы отправили вам письмо на почту'})


def check_registration(request, unique_hash):
    print(unique_hash)
    if get_or_none(User, tmp_url=unique_hash):

        u = User.objects.get(tmp_url=unique_hash)
        cookie = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
        u.logged_in_cookie = cookie
        u.save()

        response = render(request, "profile.html")  # django.http.HttpResponse
        response.set_cookie(key='logged_in_cookie', value=cookie)
        return response

    return render(request, "message.html", {'message': 'Проверьте ссылку которая вам пришла на почту'})


def profile(request):
    if get_or_none(User, logged_in_cookie=request.COOKIES.get('logged_in_cookie')):
        return render(request, "profile.html")
    return render(request, "login.html")
