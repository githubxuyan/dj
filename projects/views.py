from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse('<h1>别说了！我最好看！</h1>')
    # return render("index.html")

