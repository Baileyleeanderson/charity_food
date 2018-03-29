from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^donor$', views.donor),
    url(r'^donate/home$', views.donate_render),
    url(r'^donations/all$', views.donations_all),
    url(r'^submit_donatation$', views.submit_donation) # make sure to add user.id after login is avail
]
# (?P<donor_id>\d+)