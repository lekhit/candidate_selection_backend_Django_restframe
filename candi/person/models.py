from django.db import models

# Create your models here.
class Person(models.Model):
  Fname=models.CharField(max_length=128,blank=True)
  Lname=models.CharField(max_length=128,blank=True)
  Resume=models.FileField(upload_to='uploads/%Y/%m/%d/',max_length=256,blank=True)
  #optional: could make it unique to ensure no fake accounts 
  Contact_Number=models.CharField(max_length=10,blank=True)
  Email=models.EmailField(blank=True)
  Status=models.BooleanField(default=True)
  About = models.TextField(blank=True,null=True)
  Experience=models.TextField(blank=True,null=True)
  Educational_details=models.CharField(blank=True,max_length=256)

  def __str__(self):
    dic={'Fname':self.Fname,'Lname':self.Lname,'Contact_Number':self.Contact_Number,
          'Email':self.Email,'Status':self.Status,'About':self.About
          }
    return str(dic)