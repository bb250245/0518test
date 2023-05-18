from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime

import random

def hello(request):
    #return HttpResponse("Hello World")
    return render(request, 'myapp/hello.html')

def hello1(request, username):
    now = datetime.now()
    return render(request, 'myapp/hello1.html', locals())
    
times = 0
def hello2(request, username):
    global times
    times = times + 1
    local_times = times
    now = datetime.now()

    dicenum1 = random.randint(1,6)
    dicenum2 = random.randint(1,6)
    dicenum3 = random.randint(1,6)
    dict1 = {"dice1":dicenum1,"dice2":dicenum2,"dice3":dicenum3}

    score = random.randint(1,100)

    return render(request, 'myapp/hello2.html',locals())

def students(request):
    std1 = {"name": "Amy", "sid": "123450", "age": 18}
    std2 = {"name": "Eric", "sid": "123451", "age": 18}
    std3 = {"name": "Bryan", "sid": "123452", "age": 18}

    stds = [std1, std2, std3]    
    return render(request, 'myapp/std.html', locals())