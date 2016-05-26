from django.apps import AppConfig
from actstream import registry


# define model registrations below
class KitchenConfig(AppConfig):
    name = "dishi_kitchen"

    def ready(self):
        registry.register(self.get_model('Kitchen'))
