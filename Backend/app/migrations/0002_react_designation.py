# Generated by Django 4.2 on 2023-04-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='react',
            name='designation',
            field=models.CharField(default=True, max_length=200),
        ),
    ]