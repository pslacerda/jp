from django.db.models import *


#
# Utilitários
#

class BaseModel(Model):
    class Meta:
        abstract = True


class CreateUpdateModel(Model):
    """Um mixin para audição de datas."""

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EtcModel(Model):
    """Um mixin para adicionar um campo de observação."""

    etc = TextField(max_length=1000, blank=True, default='')

    class Meta:
        abstract = True


#
# Modelos de Negócio
#

class Product(BaseModel, CreateUpdateModel):

    description = CharField(max_length=200)

    def __str__(self):
        return self.description


class Customer(BaseModel, CreateUpdateModel, EtcModel):

    name = CharField(max_length=200)
    nickname = CharField(max_length=200, blank=True, default='')
    cpf = CharField(max_length=11, blank=True, default='')
    telephone = CharField(max_length=11, blank=True, default='')
    street = CharField(max_length=200, blank=True, default='')
    district = CharField(max_length=50, blank=True, default='')
    city = CharField(max_length=50, blank=True, default='')

    trigram_index = CharField(max_length=200+200+11+11+50+50, blank=True, null=True)

    def __str__(self):
        if self.nickname:
            return f'{self.name} ({self.nickname})'
        return self.name


class Sale(BaseModel, CreateUpdateModel, EtcModel):

    customer = ForeignKey(Customer, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)
    amount = FloatField()
    date = DateField()

    def __str__(self):
        return f'{self.customer.name} | {self.product.description}'


class Payment(BaseModel, CreateUpdateModel):
    sale = ForeignKey(Sale, on_delete=CASCADE)
    amount = FloatField()
    date = DateField()

    def __str__(self):
        return f'{self.sale} | {self.amount} | {self.date}'