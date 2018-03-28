from django.shortcuts import render, redirect

def index(request):
    return render(request,'donate/index.html')

# Create your views here.
