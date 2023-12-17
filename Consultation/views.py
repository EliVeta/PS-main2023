from django.shortcuts import render, HttpResponse
from django.views.generic import View, DeleteView, DetailView
from .forms import *
from Authorization.forms import *
from datetime import datetime
from django.utils import dateformat
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods
from django.core import mail
from PsychologicalService import settings
from datetime import date


class AppointmentConsultationInfo(View):

    def get(self, request):
        appointments = Appointment.objects.filter(id_user_id=request.user.id)


        return render(request, "Consultation/appointment_info.html", locals())





class AppointmentConsultationDelete(DeleteView):
    model = Appointment
    success_url = '/'
    template_name = 'Consultation/deleteappointment.html'
    context_object_name = 'oneappoidel'




class AppointmentConsultation(View):
    def post(self, request):
        kwargs = {}
        if 'id_locations' in request.POST.keys() and request.POST.get('id_locations') != '':
            kwargs['id_locations'] = request.POST.get('id_locations')
        id_psychologist = request.POST.get('id_psychologist')
        date = request.POST.get('date')
        time = request.POST.get('time')
        consultations = Consultation.objects.filter(**kwargs, id_psychologist=id_psychologist,
                                                    date=date, time=time)
        if consultations.exists():
            consultation = consultations.first()
            formFormat = AppointmentForm(request.POST)
            form = formFormat.save(commit=False)
            form.id_user = User.objects.get(id=request.user.id)
            form.id_consultation = consultation
            form.save()
            consultation.is_busy = True
            consultation.save()
            message = f"Вы записаны на консультацию\n Дата: {consultations.first().date.strftime('%d.%m.%Y')}\n" \
                      f"Время: {consultations.first().time}\nПсихолог: {consultations.first().id_psychologist}\n " \
                      f"Адрес: {consultations.first().id_locations.address}\n" \
                      f"Проблема: {request.POST.get('text')}"
            recipients = ['ps-sluzhba@mail.ru', request.user.username]
            msg = mail.EmailMessage(f'Запись на прием.', message, settings.EMAIL_HOST_USER, recipients)
            print(msg)
            #msg.send()
            return HttpResponseRedirect(reverse('appointment_info_table'))

    def get(self, request):
        formFormat = AppointmentForm()
        formConsultation = ConsultationForm()

        print(request.headers.get('x-requested-with'))
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dates_list = [('', '-------')]
            time_list = [('', '-------')]
            consultations = Consultation.objects.filter(is_busy=False)

            # Формат консультации
            if request.GET.get('format') != '':
                formFormat.fields['format'].initial = request.GET.get('format')
            print('строчка 180')
            # Адрес приема
            if 'id_locations' in request.GET.keys() and request.GET.get('id_locations') != '':
                formConsultation.fields['id_locations'].initial = Location.objects.get(
                    id=int(request.GET.get('id_locations')))
                consultations = consultations.filter(id_locations=int(request.GET.get('id_locations')))
            else:
                consultations = Consultation.objects.filter(is_busy=False)
            print('строчка 88')
            # Психологи
            psychologists = Psychologist.objects.filter(
                id__in=[psychologist.id_psychologist.id for psychologist in consultations])
            formConsultation.fields['id_psychologist'].queryset = psychologists
            if 'id_psychologist' in request.GET.keys() and request.GET.get('id_psychologist') != '':
                formConsultation.fields['id_psychologist'].initial = Psychologist.objects.get(
                    id=int(request.GET.get('id_psychologist')))
                consultation_psychologist = consultations.filter(
                    id_psychologist=int(request.GET.get('id_psychologist')))
                for d in consultation_psychologist:
                    if (d.date, d.date.strftime('%d.%m.%Y')) not in dates_list:
                        dates_list.append((d.date, d.date.strftime('%d.%m.%Y')))
                formConsultation.fields['date'].choices = dates_list

                # Дата приема
                if 'date' in request.GET.keys() and request.GET.get('date') != '':
                    formConsultation.fields['date'].initial = request.GET.get('date')
                    consultation_psychologist = consultation_psychologist.filter(date=request.GET.get('date'))
                    for i, t in enumerate(consultation_psychologist):
                        time_list.append((t.time, t.time))

                    # Время приема
                    if 'time' in request.GET.keys() and request.GET.get('time') != '':
                        formConsultation.fields['time'].initial = request.GET.get('time')
                    formConsultation.fields['time'].choices = time_list
            return JsonResponse({
                "result": True,
                "forms": render_to_string(
                    request=request,
                    template_name='Consultation/appointment_form.html',
                    context={
                        "title": "Запись",
                        'formFormat': formFormat,
                        'formConsultation': formConsultation,
                    }
                )
            })
        else:
            print('строчка 127')

            return render(request=request,
                          template_name='Consultation/appointment.html',
                          context={
                              "title": "Запись",
                              'formFormat': formFormat,
                              'formConsultation': formConsultation,
                          })
