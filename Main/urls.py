from django.template.defaulttags import url
from django.urls import re_path, path, include
from Main.views import *

urlpatterns = [
    #re_path(r"^$", AppointmentConsultation.as_view(), name="appointment_consultation"),
    path("", Main.as_view(), name='main'),


    #path('', include('Authorization.urls'), name='registr'),
    #path('registration/', include('Authorization.urls'), name='registr'),
    #path('login/', include('Authorization.urls'), name='log'),
    #path('registration/', Registration.as_view(), name='registr'),
    #path('login/', Login.as_view(), name='log'),


]
