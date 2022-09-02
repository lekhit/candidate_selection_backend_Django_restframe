from django.db import models

# Create your models here.
class Person(models.Model):
  Fname=models.CharField(max_length=128)
  Lname=models.CharField(max_length=128)
  Resume=models.FileField(upload_to='uploads/% Y/% m/% d/',max_length=256,null=True,blank=True)
  #optional: could make it unique to ensure no fake accounts 
  Contact_Number=models.DecimalField(max_digits=10,decimal_places=0,blank=True,null=True)
  Email=models.EmailField()
  Status=models.BooleanField(default=True)
  About = models.TextField(blank=True,null=True)

  def __str__(self):
    dic={'Fname':self.Fname,'Lname':self.Lname,'Contact_Number':self.Contact_Number,
          'Email':self.Email,'Status':self.Status,'About':self.About
          }
    return str(dic)