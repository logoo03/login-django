import json

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

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
            return HttpResponse('No input id.')
        if (not password):
            return HttpResponse('No input password.')

        if (user_id != user_data['id']):
            return HttpResponse('Invalid Username.', status=401)
        elif (password != user_data['password']):
            return HttpResponse('Invalid Password.', status=401)
        else:
            return HttpResponse('<h3 style="color:blue;">Login Success!</h3>')

    data = json.dumps(req.GET)
    return HttpResponse(f"""This is the main login page. <br>
                        method: {req.method} <br>
                        data: {data}""")

def login_detail(req, id):
    return HttpResponse(f'Your user ID is \'{id}\'.')
