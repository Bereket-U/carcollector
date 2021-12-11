# Generated by Django 3.2.9 on 2021-12-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(verbose_name='Service date'),
        ),
    ]