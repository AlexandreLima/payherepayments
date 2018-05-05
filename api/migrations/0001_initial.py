# Generated by Django 2.0.3 on 2018-05-05 00:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adquirer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('key_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('cnpj', models.CharField(max_length=40)),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aquirer_name', models.CharField(max_length=500)),
                ('aquirer_key', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=500)),
                ('holder_name', models.CharField(max_length=500)),
                ('holder_document_number', models.CharField(max_length=500)),
                ('expiration_date', models.CharField(max_length=500)),
                ('securityCode', models.CharField(max_length=500)),
                ('token', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=20)),
                ('document_type', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('unit_amount_in_cents', models.IntegerField()),
                ('total_amount_in_cents', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recurrency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('frequency', models.IntegerField()),
                ('start_billing_date', models.DateField()),
                ('end_billing_date', models.IntegerField()),
                ('amount_in_cents', models.IntegerField()),
                ('installment_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.Sale'),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditcards', to='api.Sale'),
        ),
    ]