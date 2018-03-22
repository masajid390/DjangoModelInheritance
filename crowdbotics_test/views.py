from django.http import HttpResponse


def home(request):
    html = "<html><body><h1>Welcome to Crowdbotics</h1><a href='/api/crowbotics/animal/?type=cat'>Cat CRUD APIs" \
           "</a></br><a href='/api/crowbotics/animal/?type=dog'>Dog CRUD APIs</a>"
    return HttpResponse(html)
