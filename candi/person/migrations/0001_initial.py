# Generated by Django 4.0.7 on 2022-09-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=128)),
                ('Lname', models.CharField(max_length=128)),
                ('Resume', models.FileField(blank=True, max_length=256, null=True, upload_to='uploads/% Y/% m/% d/')),
                ('Contact_Number', models.DecimalField(blank=True, decimal_places=0, max_digits=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Status', models.BooleanField(default=True)),
                ('About', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
