from django.shortcuts import render, redirect

def home(request):
    context={  
    }
    return render(request, 'generator/home.html', context)

def about(request):
    context={
    }
    return render(request, 'generator/about.html', context)


