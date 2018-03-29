from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^charity$', views.charity),
    url(r'^success$', views.payment_form),
    url(r"^checkout$", views.checkout)
]
