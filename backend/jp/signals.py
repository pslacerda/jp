import re

from django.dispatch import receiver
from unidecode import unidecode

from jp.app import customer_updated
from jp.models.models import Customer


@receiver(customer_updated)
def update_trigram_index(**kwargs):
    def _(field):
        return field + " "
    customer = kwargs['instance']
    customer.trigram_index = re.sub(r'\s+', ' ', unidecode((
        _(customer.name) +
        _(customer.nickname) +
        _(customer.telephone) +
        _(customer.cpf) +
        _(customer.district) +
        _(customer.city)
    ).lower()))
    customer.save()
