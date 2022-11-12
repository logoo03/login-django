import json

from django.shortcuts import render
from django.http import HttpResponse

def login(req):
    user_data = {
        'id': 'python',
        'password': 'django',
    }

    if (req.method == 'GET'):
        user_id = req.GET['id']
        password = req.GET['pw']

        if (user_id != user_data['id']):
            return HttpResponse('Invalid Username.', status=401)
        elif (password != user_data['password']):
            return HttpResponse('Invalid Password.', status=401)
        else:
            return HttpResponse('Login Success!')

    data = json.dumps(req.GET)
    return HttpResponse(f"""This is the main login page. <br>
                        method: {req.method} <br>
                        data: {data}""")

def login_detail(req, id):
    return HttpResponse(f'Your user ID is \'{id}\'.')
