from django.apps import AppConfig
# from . import signals

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self) :
        import app.signals
   