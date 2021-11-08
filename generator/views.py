from django.shortcuts import render, redirect

import random

def home(request):
    context={  
    }
    return render(request, 'generator/home.html', context)

def about(request):
    context={
    }
    return render(request, 'generator/about.html', context)

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password_generated = ''

    pass_lenght = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special_chars'):
        characters.extend(list('-_!#$%&/()=?¡'))

    for x in range(pass_lenght):
        password_generated += random.choice(characters)

    context={
        'password' : password_generated
    }
    return render(request, 'generator/password.html', context)

