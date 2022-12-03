import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.utils.datastructures import MultiValueDictKeyError

from users.models import User


def index(req):
    return render(req, 'index.html')


def login(req):
    if (req.method == 'GET'):
        return render(req, 'users/login.html')

    if (req.method == 'POST'):
        user_id = req.POST.get('id')
        password = req.POST.get('pw')

        if (not user_id):
            return render(req, 'users/input_blank.html', {'data': 'userid'})
        if (not password):
            return render(req, 'users/input_blank.html', {'data': 'password'})

        try:
            user = User.objects.get(user_id=user_id, password=password)
            res = redirect('pages:index')
            res.set_cookie('user_id', user_id)
            res.set_cookie('password', password)
            res.set_cookie('authorized', True)

            return res

        except User.DoesNotExist:
            return render(req, 'users/unauthorized.html', status=401)


def logout(req):
    res = redirect('pages:index')
    res.delete_cookie('authorized')

    return res


def login_detail(req, id):
    return HttpResponse(f'Your user ID is \'{id}\'.')


def register(req):
    if req.method == 'GET':
        return render(req, 'users/register.html')
    elif req.method == 'POST':
        user_id = req.POST.get('id')
        password = req.POST.get('pw')

        # Check Blanks
        if not (user_id):
            return render(req, 'users/register.html', {'blank': True, 'type': 'user_id'})
        elif not (password):
            return render(req, 'users/register.html', {'blank': True, 'type': 'password'})

        # Check Duplicates
        try:
            _ = User.objects.get(user_id=user_id)
            return render(req, 'users/register.html', {'exist': True})
        except User.DoesNotExist:
            pass

        # Register Success
        user = User(user_id=user_id, password=password)
        user.save()

        res = redirect('pages:index')
        res.set_cookie('user_id', user_id)
        res.set_cookie('password', password)
        res.set_cookie('authorized', True)

        return res
