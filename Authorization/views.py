#from django.contrib.auth.forms import AuthenticationForm
import re

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import *
from django.contrib.auth.hashers import make_password
from random import randint
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RegisterSignupForm
from datetime import datetime
from django.utils import dateformat
#from  .utils import hadle_uploaded_file
from django.views.generic.edit import CreateView



# Create your views here.

class Registration(View):

    def get(self, request):
        form = RegisterUserForm(request.POST, request.FILES)
        code = randint(101, 999)
        global cod_captcha
        cod_captcha = str(code)

        context={
            'title': 'Регистрация',
            'form': form,
            'captcha': cod_captcha
        }
        return render(request, "Authorization/registration.html", context=context)

    def post(self, request):
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            #еще нет проверки на уникальность вводимого емайла!!!

            captcha = request.POST.get('captcha')
            if cod_captcha==str(captcha):

                if form.cleaned_data['password']==form.cleaned_data['password2']:
                    userdata = form.save(commit=False)
                    userdata.password = make_password(form.cleaned_data['password2'])
                    userdata.save()

                    if userdata.id is not None:
                        user = User.objects.get(pk=userdata.id)
                        userRight = UserRight()
                        userRight.id_user = user
                        right = Right.objects.get(pk=1)
                        userRight.id_right = right
                        userRight.save()
                    #return reversed('main')
                    #return reverse_lazy('main')
                    return HttpResponse('Всё четко. Жми стрелочку НАЗАД в браузере. Разработчики это фиксят')
                else:
                    return HttpResponse('Пароли не совпали, нажмите стрелочку НАЗАД в браузере — создатели сайта еще не додумались как не перебрасывать на эту страницу при несовпадении паролей :0')
            else:
                #return reverse_lazy('registr')
                return HttpResponse('Лучше на капчу смотрите:)')


class Login(LoginView):

    def get(self, request):
        form = LoginForm

        context = {
            'title': 'Вход',
            'form': form,
        }
        return render(request, "Authorization/login.html", context=context)


    def post(self, request):
        pass


class LoginDjango(LoginView):


    form_class = LoginForm
    template_name = 'Authorization/login.html'

    def get_success_url(self):

        return reverse_lazy('main')


class RegistrationSinqup(CreateView):
    try:
        #form = ExtendedRegisterSignupForm
        form_class = RegisterSignupForm
        template_name = "Authorization/registration.html"
        success_url = reverse_lazy('log')
    except:
        def validEmail(self, request):
            data = {}
            email = request.POST.get('username')
            result = re.search(r'[\w\.-]+@[\w-]+\.[\w]{2,4}', email)
            if result:
                data = {
                    'message': 'Email указан <b style="color: green;">правильно</b>!',
                    'match': result.group(0)
                }
            else:
                data = {
                    'message': 'Email указан <b style="color: red;">некорректно</b>!',
                }
                return JsonResponse(data)





def userLogout(request):
    logout(request)
    return redirect('main')