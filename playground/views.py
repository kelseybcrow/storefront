from django.shortcuts import render
from django.http import HttpResponse

# views aren't actually views, they're request handlers. What other frameworks call views are called templates in django
# Create your views here.
# request -> response
# request handler
# action


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Kelsey'})
