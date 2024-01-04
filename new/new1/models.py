from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class student(models.Model):
    def __str__(self):
        return self.name    
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    marks=models.FloatField()
    #section=models.CharField(max_length=20)
    pics=models.CharField(max_length=1000,default='https://th.bing.com/th/id/OIP.kqT6XFsG2BTW22Y4st2-KAHaHa?pid=ImgDet&rs=1')
    def get_absolute_url(self):
        return reverse('new1:studentid', kwargs={'pk': self.pk})
    