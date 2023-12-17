from django.shortcuts import render, HttpResponse
from django.views.generic import View
from Psychologist.models import Psychologist

from .models import CommentsPost
from django.forms import forms
#from .forms import CommentForm

#from .forms import *
from datetime import datetime
from django.utils import dateformat
#from  .utils import hadle_uploaded_file

# Create your views here.

class Main(View):

    def post(self,request):
        pass

    def get(self, request):
        psychologist = Psychologist.objects.all()
        context ={
            'title': 'Главная',
            'psychologist': psychologist,
        }
        return render(request, "Main/main.html", context=context)


class Comment(View):
    
    def post(self,request):
        pass
    
    def get(self,request):
        comment = CommentsPost.objects.all()
        context = {
            'comment': comment,
            'ro': 'roro'
        }
        return render(request, "Main/main.html", context=context)






















'''
class Registration(View):
    def post(self,request):
        pass

    def get(self, request):

        context = {
            'title': 'Регистрация',
        }
        return render(request, "Main/registration.html", context=context)


class Login(View):
    def post(self,request):
        pass

    def get(self, request):

        context = {
            'title': 'Вход',
        }
        return render(request, "Main/login.html", context=context)
'''
