from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
from datetime import datetime
import re
import bcrypt
 
# import stripe


def index(request):
    return render(request,'donate/index.html')

def logout(request):
    del request.session['id']
    return redirect('/')

def donor(request):
    return redirect('/donate/home')

def donations_all(request):
    context = {  
        'foods': Food.objects.all(),
        'charities': Charity.objects.all()
             
    }
    return render(request,'donate/all_donations.html',context)

def charity(request):
    context = {
        'user': Charity.objects.get(id=request.session['id']),
        'restaurants': Donor.objects.all(),
        'cities': City.objects.all(),
        'states': State.objects.all(),
        'charities': Charity.objects.all(),
        'picks': Food.objects.all().exclude(charity=request.session['id']),
        'baskets': Food.objects.filter(charity=request.session['id'])
    }

    return render(request,"donate/charity.html", context)

def add(request, id):
    this_charity = Charity.objects.get(id=request.session['id'])
    this_food = Food.objects.get(id=id)
    this_food.charity.add(this_charity)
    
    return redirect("/charity")

def donate_render(request):
    if not 'id' in request.session:
        return redirect("/")
    context = {
        'donators': Donor.objects.get(id=request.session['id'])
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

    food = Food.objects.create(food_name=request.POST['food'],type_of_food=request.POST['category'],pickup=request.POST['date'],pickup_time=request.POST['time'])
    donor = Donor.objects.get(id=request.session['id'])
    food.donor = donor
    food.save()
    context = {
        'donators': Donor.objects.first()
    }
    return redirect('/donate/home')

def register_business(request):
    if request.method == "POST":
        # validations
        state_regex = re.compile(r'^[A-Z]$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        error = False
        if len(request.POST['name']) < 1:
            error = True
            messages.error(request, "Business name field must not be empty")
        if len(request.POST['contact']) < 1:
            error = True
            messages.error(request, "Contact name field must not be empty")
        if not len(request.POST['phone']) == 10:
            error = True
            messages.error(request, "Phone number field must not be empty")
        if len(request.POST['address']) < 1:
            error = True
            messages.error(request, "Address field must not be empty")
        if len(request.POST['city']) < 1:
            error = True
            messages.error(request, "City field must not be empty")
        if not len(request.POST['state']) == 2 and state_regex.match(request.POST['state']):
            error = True
            messages.error(request, "Please use state abbreviation")
        if len(request.POST['email']) < 1:
            error = True
            messages.error(request, "Email field must not be empty")
        elif not email_regex.match(request.POST['email']):
            error = True
            messages.error(request, "Invalid email")
        if len(request.POST['password']) < 1:
            error = True
            messages.error(request, "Password must not be empty")
        elif len(request.POST['password']) < 4:
            error = True
            messages.error(request, "Password must be at least 5 characters")
        if not request.POST['password'] == request.POST['confirm_pw']:
            error = True
            messages.error(request, "Passwords do not match")

        if error:
            return redirect('/')
        
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        newDonor = Donor.objects.create(business_name = request.POST['name'],contact_name = request.POST['contact'], phone_number = request.POST['phone'], email = request.POST['email'],password = hashed, admin_level = 1, address=request.POST['address'])

        cityList = City.objects.filter(city = request.POST['city'])
        if len(cityList) > 0:  #Check for city in DB
            oldcity = cityList[0]
            newDonor.city = oldcity
        else:
            newCity = City.objects.create(city=request.POST['city'])
            newDonor.city = newCity
        stateList = State.objects.filter(state = request.POST['state'])
        if len(stateList) > 0: #Check for state in DB
            oldState = stateList[0]
            newDonor.state = oldState
        else:
            newState = State.objects.create(state=request.POST['state'])
            newDonor.state = newState
        newDonor.save()
        request.session['id'] = newDonor.id
        return redirect ('/donor')
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        donorList = Donor.objects.filter(email = request.POST['login_email'])
        if len(donorList) > 0:
            donor = donorList[0]
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/')

        if bcrypt.checkpw(request.POST['login_password'].encode(),donor.password.encode()):
            request.session['id'] = donor.id
            return redirect('/donor')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/')
    else:
        return redirect('/')
    
def register_charity(request):
    if request.method == "POST":
        # validations
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        error = False
        if len(request.POST['name']) < 1:
            error = True
            messages.error(request, "Business name field must not be empty")
        if len(request.POST['contact']) < 1:
            error = True
            messages.error(request, "Contact name field must not be empty")
        if len(request.POST['phone']) < 1:
            error = True
            messages.error(request, "Phone number field must not be empty")
        if len(request.POST['address']) < 1:
            error = True
            messages.error(request, "Address field must not be empty")
        if len(request.POST['city']) < 1:
            error = True
            messages.error(request, "City field must not be empty")
        if not len(request.POST['state']) == 2:
            error = True
            messages.error(request, "Please use state abbreviation")
        if len(request.POST['email']) < 1:
            error = True
            messages.error(request, "Email field must not be empty")
        elif not email_regex.match(request.POST['email']):
            error = True
            messages.error(request, "Invalid email")
        if len(request.POST['password']) < 1:
            error = True
            messages.error(request, "Password must not be empty")
        elif len(request.POST['password']) < 4:
            error = True
            messages.error(request, "Password must be at least 5 characters")
        if not request.POST['password'] == request.POST['confirm_pw']:
            error = True
            messages.error(request, "Passwords do not match")

        if error:
            return redirect('/')
        
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        newCharity = Charity.objects.create(charity_name = request.POST['name'],contact_name = request.POST['contact'], phone_number = request.POST['phone'], email = request.POST['email'],password = hashed, admin_level = 2,address=request.POST['address'])

        cityList = City.objects.filter(city = request.POST['city'])
        if len(cityList) > 0:  #Check for city in DB
            oldcity = cityList[0]
            newCharity.city = oldcity
        else:
            newCity = City.objects.create(city=request.POST['city'])
            newCharity.city = newCity
        stateList = State.objects.filter(state = request.POST['state'])
        if len(stateList) > 0: #Check for state in DB
            oldState = stateList[0]
            newCharity.state = oldState
        else:
            newState = State.objects.create(state=request.POST['state'])
            newCharity.state = newState
        newCharity.save()
        request.session['id'] = newCharity.id
        return redirect ('/charity')
    else:
        return redirect('/')

def payment_form(request):
    return render(request, "donate/success.html")

def checkout(request):
    stripe.api_key = "pk_test_OlNSLZe6l3rBBnfUkT2KIui7"
    return redirect("/charity")
