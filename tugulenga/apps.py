from django.apps import AppConfig


class TugulengaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tugulenga'
    def ready(self):
        import tugulenga.signals
