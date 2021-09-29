from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class RollindustriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rollindustries'
    verbose_name = 'Roll Industries'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'