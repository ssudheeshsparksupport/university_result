from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import Staff,Student,Result
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        print "AAAAAAAAAAAAAaaaaaaa"
        return render(request,'university/home.html')

class StaffRegisterView(View):

    def get(self, request):
        print request
        return render(request,'university/staff_register.html')

    @csrf_exempt
    def post(self, request):
        
        user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        obj=Staff()
        obj.firstname = request.POST['username']
        obj.email = request.POST['email']
        obj.password = request.POST['password']
        obj.user = user
        obj.save()
        return HttpResponse()

        StaffLoginView

class StaffLoginView(View):
    print "AAAAAAa"

    def get(self, request):
        print "getttt"

    @csrf_exempt
    def post(self, request):
        print "posttttt"
    
    




