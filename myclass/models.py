from django.db import models

# Create your models here.

class studentData(models.Model):
    name =models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    rollno = models.IntegerField()
    age =models.IntegerField()
    fathersname =models.CharField(max_length=30)
    

    def __str__(self):
        return self.name +"/"+ self.grade