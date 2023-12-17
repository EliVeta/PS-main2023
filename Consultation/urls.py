from django.urls import re_path, path
from Consultation.views import *

urlpatterns = [
    # re_path(r"^$", AppointmentConsultation.as_view(), name="appointment"),
    path("appointment_info/", AppointmentConsultation.as_view(), name="appointment_info"),
    path("appointment_info_table/", AppointmentConsultationInfo.as_view(), name="appointment_info_table"),
    path("<int:pk>/delete", AppointmentConsultationDelete.as_view(), name='deleteappoi'),

]
