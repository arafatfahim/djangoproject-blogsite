from django.db import models

# Create your models here.

class Contact(models.Model):
    #database table name
    contactid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default=None)
    phone = models.CharField(max_length=13, default=None)
    email = models.EmailField(max_length=100, default=None)
    msg = models.TextField(max_length=5000, default=None)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    #showing sender name without pressing the message
    def __str__(self):
        return  self.name + '-' + '(' + self.email + ')'

