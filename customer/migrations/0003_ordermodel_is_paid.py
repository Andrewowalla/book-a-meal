# Generated by Django 4.0.3 on 2022-04-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_ordermodel_city_ordermodel_email_ordermodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
