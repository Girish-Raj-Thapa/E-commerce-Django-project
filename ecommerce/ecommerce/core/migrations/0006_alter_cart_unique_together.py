# Generated by Django 5.1 on 2024-08-20 11:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
    ]
