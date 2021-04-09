from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from jp.models.models import Customer, Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['description']
        labels = {
            'description': _('Descrição')
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name', 'nickname', 'cpf', 'telephone',
            'street', 'district', 'city'
        ]
        labels = {
            'name': _('Nome'),
            'nickname': _('Apelido'),
            'cpf': _('C.P.F.'),
            'telephone': _('Telefone'),
            'street': _('Rua'),
            'district': _('Bairro'),
            'city': _('Cidade'),
        }