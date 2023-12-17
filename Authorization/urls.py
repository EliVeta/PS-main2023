from Authorization.views import *
from django.urls import path, include
from Authorization import views


urlpatterns = [
    path('registration/', RegistrationSinqup.as_view(), name="registr"),
    path('login/', LoginDjango.as_view(), name="log"),
    path('logout/', views.userLogout, name='logout'),

    path('jqajax/checkemail/', RegistrationSinqup.as_view(), name='jquery_ajax_checkemail'),

    #path('registration/', CreatePsychologistView.as_view(), name="registr"),

]