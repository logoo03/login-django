import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.utils.datastructures import MultiValueDictKeyError

def login(req):
    user_data = {
        'id': 'python',
        'password': 'django',
    }
    
    if (req.method == 'GET'):
        return render(req, 'users/login.html')

    if (req.method == 'POST'):
        user_id = req.POST.get('id')
        password = req.POST.get('pw')

        if (not user_id):
            return render(req, 'users/input_blank.html', {'data': 'userid'})
        if (not password):
            return render(req, 'users/input_blank.html', {'data': 'password'})

        if (user_id != user_data['id']):
            return render(req, 'users/unauthorized.html', {'data': 'userid'}, status=401)
        elif (password != user_data['password']):
            return render(req, 'users/unauthorized.html', {'data': 'password'}, status=401)
        else: # Login Success
            res = redirect('pages:index')
            res.set_cookie('user_id', user_id)
            res.set_cookie('password', password)
            res.set_cookie('authorized', True)
            
            return res

def login_detail(req, id):
    return HttpResponse(f'Your user ID is \'{id}\'.')
