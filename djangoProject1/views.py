from django.shortcuts import render


def index(request):
    context = {'name':'Rekruto', 'message':'Давай дружить'}
    req = request.GET
    name = req.get('name')
    message = req.get('message')
    context = {'name': name, 'message': message}
    return render(request, 'index.html', context)
