# Generated by Django 5.0.2 on 2024-02-26 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_alter_user_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]