from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
from datetime import datetime

def index(request):
    request.session['id']= '1'
    return render(request,'donate/index.html')

def donor(request):
    return redirect('/donate/home')

def donations_all(request):
    context = {
        'posts': Post.objects.all()
        
    }
    return render(request,'donate/all_donations.html',context)

def donate_render(request):
    context = {
        'donators': Donor.objects.first()
    }
    return render(request,'donate/donate.html',context)

def submit_donation(request):
    errors = False
    if request.POST['food'] == '':
        messages.error(request,'Please enter type of Food')
        errors = True
    if request.POST['date'] < str(datetime.now()):
        messages.error(request,'Please enter a future date')
        errors = True
    if errors:
        return redirect('/donate/home')
    request.session['id']= '1'
    Food.objects.create(food_name=request.POST['food'],type_of_food=request.POST['category'])
    Post.objects.create(pickup=request.POST['date'],pickup_time=request.POST['time'])
    context = {
        'donators': Donor.objects.first()
    }
    return redirect('/donate/home')



