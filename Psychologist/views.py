from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .forms import *
from Consultation.forms import *
from Consultation.models import Location, Consultation



class CreatePsychologistView(View):

    def get(self, request):
        formPsychologist = PsychologistForm(request.POST, request.FILES)
        formUrl = UrlToOnlineConsultationForm(request.POST)
        formLocation = LocationForm(request.POST)
        formConsultation = ConsultationForm(request.POST)

        context = {
            'formPsychologist': formPsychologist,
            'formUrl': formUrl,
            'formLocation': formLocation,
            'formConsultation': formConsultation
        }
        return render(request, 'Psychologist/create_psychologist.html', context=context)

    def post(self, request):
        formPsychologist = PsychologistForm(request.POST, request.FILES)

        if formPsychologist.is_valid():
            psychologistData = formPsychologist.save(commit=True)

            if psychologistData.id is not None:
                psychologist = Psychologist.objects.get(pk=psychologistData.id)



                formLocation = LocationForm(request.POST)
                if  formLocation.is_valid():
                    locationData = formLocation.save(commit=True)

                    if locationData.id is not None:
                        location = Location.objects.get(pk=locationData.id)

                        formConsultation = ConsultationForm(request.POST)
                        if formConsultation.is_valid():
                            print(1)
                            consultationData = formConsultation.save(commit=False)
                            consultationData.id_psychologist_id = psychologist.id
                            consultationData.id_locations_id = location.id
                            consultationData.save()

                formUrl = UrlToOnlineConsultationForm(request.POST)
                if formUrl.is_valid():
                    urlData = formUrl.save(commit=False)
                    urlData.id_psychologist_id = psychologist.id
                    urlData.save()


            return HttpResponse("<h4>YOUR FORM HAS BEEN SUCCESSFULLY SUBMITED</h4>")
        else:
            return HttpResponse("<h4>Неверно введены данные</h4>")