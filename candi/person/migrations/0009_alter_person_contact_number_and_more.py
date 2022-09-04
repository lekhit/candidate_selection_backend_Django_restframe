# Generated by Django 4.0.7 on 2022-09-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_alter_person_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Contact_Number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='Educational_details',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='person',
            name='Email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='Fname',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='person',
            name='Lname',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
