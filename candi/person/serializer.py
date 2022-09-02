from rest_framework import serializers
from .models import Person

'''Fname=models.CharField(max_length=128)
  Lname=models.CharField(max_length=128)
  Resume=models.FileField(upload_to='uploads/% Y/% m/% d/',max_length=256,null=True,blank=True)
  #optional: could make it unique to ensure no fake accounts 
  Contact_Number=models.DecimalField(max_digits=10,decimal_places=0,blank=True,null=True)
  Email=models.EmailField()
  Status=models.BooleanField(default=True)
  About = models.TextField(blank=True,null=True)
  Experience=models.TextField(blank=True,null=True)
  Educational_details=models.CharField(max_length=256)

'''

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model =Person
    fields=['Fname',
    'Lname',
    "Contact_Number",
    'Email',
    'Status',
    'About',
    'Experience',
    'Educational_details'
    ]
