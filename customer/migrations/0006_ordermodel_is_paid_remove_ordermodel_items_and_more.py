# Generated by Django 4.0.3 on 2022-04-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_merge_20220405_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='items',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='order', to='customer.menuitem'),
        ),
    ]
