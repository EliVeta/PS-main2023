#from Tools.demo.mcast import sender
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from Consultation.models import Appointment



@receiver(pre_delete, sender=Appointment)
def pre_del_appoi(sender, instance, using, **kwargs):
    cons_id = instance.id_consultation
    cons_id.is_busy = False
    cons_id.save()
    print('Я работаю')


