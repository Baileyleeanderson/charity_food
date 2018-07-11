from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/business$',views.register_business),
    url(r'^register/charity$',views.register_charity),
    url(r'^login_business$',views.login_business),
    url(r'^login_charity$',views.login_charity),
    url(r'^logout$',views.logout),
    url(r'^donor$', views.donor),
    url(r'^charity$', views.charity),
    url(r'^success$', views.payment_form),
    url(r"^checkout$", views.checkout),
    url(r'^donate/home$', views.donate_render),
    url(r'^donations/all$', views.donations_all),
    url(r'^submit_donatation$', views.submit_donation),# make sure to add user.id after login is avail
    url(r'^add/(?P<id>\d+)$',views.add)
]
# (?P<donor_id>\d+)