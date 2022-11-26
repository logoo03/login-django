from django.shortcuts import render

def index(req):
    context = {
        'authorized': req.COOKIES['authorized'] or False,
        'user_id': req.COOKIES['user_id'] or None,
        'password': req.COOKIES['password'] or None,
    }
    
    return render(req, 'index.html', context)
