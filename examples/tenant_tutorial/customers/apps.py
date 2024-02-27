
from django.apps import AppConfig


class CustomersConfig(AppConfig):
    name = 'customers'
    verbose_name = 'Customers'

    def ready(self):
        import customers.handlers
