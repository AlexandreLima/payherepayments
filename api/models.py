from django.db import models
from django.utils.timezone import now
import uuid

class Sale(models.Model):
    def __init__(self, *args):
        super(Sale, self).__init__(*args)

    id =  models.AutoField(primary_key=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, null=False)
    creation_date = models.DateTimeField(default=now, editable=False,  blank=False, null=False)

        
class Customer(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    document = models.CharField(max_length=20, blank=False, null=False)
    document_type = models.CharField(max_length=3, blank=False, null=False)
    

class CreditCard(models.Model):
    id =  models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="creditcards")
    aquirer_name = models.CharField(max_length=500, blank=False, null=False)
    aquirer_key = models.CharField(max_length=500, blank=False, null=False)
    number = models.CharField(max_length=500, blank=False, null=False)
    holder_name = models.CharField(max_length=500, blank=False, null=False)
    holder_document_number = models.CharField(max_length=500, blank=False, null=False)
    expiration_date = models.CharField(max_length=500, blank=False, null=False)
    securityCode = models.CharField(max_length=500, blank=False, null=False)
    token = models.CharField(max_length=500, blank=False, null=False)
    

class Item(models.Model):
    id =  models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=500, blank=False, null=False)
    quantity = models.IntegerField(null=False)
    unit_amount_in_cents =  models.IntegerField(null=False)
    total_amount_in_cents = models.IntegerField(null=False)

class Recurrency(models.Model):
    id =  models.AutoField(primary_key=True)
    frequency = models.IntegerField(null=False)
    start_billing_date = models.DateField(null= False)
    end_billing_date = models.IntegerField(null= False)
    amount_in_cents =  models.IntegerField( null=False)
    installment_count= models.IntegerField(null=False)
    

class Adquirer(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False, blank=False)
    key_name = models.CharField(max_length=10, null=False, blank=False)


class Client(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    cnpj = models.CharField(max_length=40, null=False, blank=False)
    token = models.UUIDField(default=uuid.uuid4, editable=False, null=False)
