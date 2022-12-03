from django.shortcuts import render

def index(req):
    context = {
        'authorized': req.COOKIES.get('authorized') or False,
        'user_id': req.COOKIES.get('user_id') or None,
        'password': req.COOKIES.get('password') or None,
    }
    
    return render(req, 'index.html', context)
