# Generated by Django 3.2.8 on 2021-12-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_client_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='activity',
            field=models.BooleanField(default=False),
        ),
    ]