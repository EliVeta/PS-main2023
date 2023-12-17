from django.apps import AppConfig


class ConsultationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Consultation'

    def ready(self):
        import Consultation.signal_on_del_appoi
