# Generated by Django 2.2.1 on 2019-05-10 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('sub_inv', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Sub Inventory')),
                ('pdv', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
    ]
