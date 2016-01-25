from django.conf.urls import url
from university.views import *

urlpatterns = [

     url(r'^$', HomeView.as_view(),name='home'),
     
     url(r'^staffregister/$', StaffRegisterView.as_view(), name='staff_register'),
     # url(r'^homeone/$', views.homeone, name='homeone'),
     url(r'^stafflogin/$', StaffLoginView.as_view(), name='staff_login'),
     # url(r'^staff_view/$', views.staff_view, name='staff_view'),
     # url(r'^student_reg/$', views.student_reg, name='student_reg'),
     # url(r'^result_entry/$', views.result_entry, name='result_entry'),
     # url(r'^test/(?P<dateformat>.*?)/$', views.test, name='test'),
     # url(r'^result/$', views.result, name='result'),
     #url(r'^result_display/$', views.result_display, name='result_display'),

]