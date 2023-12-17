from django.contrib import admin
from .models import *
from . import models


class RecipeInline(admin.StackedInline):
    model = models.UrlToOnlineConsultation
    extra = 1


@admin.register(models.Psychologist)
class PsychologistAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]

# Register your models here.

admin.site.register(UrlToOnlineConsultation)