from django.shortcuts import render, redirect
from . models import *
import stripe



def index(request):

    return render(request,'donate/index.html')

def charity(request):
    
    return render(request,"donate/charity.html")

def payment_form(request):
    
   
    
    return render(request, "donate/success.html")

def checkout(request):
   

    stripe.api_key = "pk_test_OlNSLZe6l3rBBnfUkT2KIui7"
    

    return redirect("/charity")