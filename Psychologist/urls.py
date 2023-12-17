from Psychologist.views import *
from django.urls import path, include

urlpatterns = [
    path('create_psychologist/', CreatePsychologistView.as_view(), name="create_psychologist"),
]


