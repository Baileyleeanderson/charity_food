from __future__ import unicode_literals
from django.db import models
from datetime import date

class City(models.Model):
    city = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class State(models.Model):
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Donor(models.Model):
    business_name = models.CharField(max_length=80)
    contact_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length = 100)
    address = models.CharField(max_length=100,default = '')
    city = models.ForeignKey(City, related_name="donor_city",null=True)
    state = models.ForeignKey(State, related_name = "donor_state",null=True)
    admin_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Charity(models.Model):
    charity_name = models.CharField(max_length=80)
    contact_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length = 100)
    address = models.CharField(max_length=100,default = '')
    city = models.ForeignKey(City, related_name="charity_city",null=True)
    state = models.ForeignKey(State, related_name = "charity_state",null=True)
    admin_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Food(models.Model):
    food_name = models.CharField(max_length=80)
    type_of_food = models.CharField(max_length=80, default='')
    donor = models.ForeignKey(Donor, related_name='foods',null=True)
    charity = models.ManyToManyField(Charity, related_name='foods')
    pickup = models.DateField(max_length=8,default='')
    pickup_time = models.CharField(max_length=10,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
