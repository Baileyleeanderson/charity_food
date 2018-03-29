from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/business$',views.register_business),
    url(r'^register/charity$',views.register_charity),
    url(r'^login$',views.login),
    url(r'^donor$',views.donor),
    url(r'^charity$', views.charity)
]
