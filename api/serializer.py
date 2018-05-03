from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from models import Sale, Client, CreditCard, Customer, Adquirer, Item, Recurrency

class SaleSerializer(serializer.ModelSerializer):
    class Meta:
        model = Sale

class ClientSerializer(serializer.ModelSerializer):
    class Meta:
        model = Client

class SaleSerializer(serializer.ModelSerializer):
    class Meta:
        model = Sale

class CreditCardSerializer(serializer.ModelSerializer):
    class Meta:
        model = CreditCard

class CustomerSerializer(serializer.ModelSerializer):
    class Meta:
        model = Customer

class AdquirerSerializer(serializer.ModelSerializer):
    class Meta:
        model = Adquirer

class ItemCardSerializer(serializer.ModelSerializer):
    class Meta:
        model = Item

class RecurrencySerializer(serializer.ModelSerializer):
    class Meta:
        model = Recurrency
