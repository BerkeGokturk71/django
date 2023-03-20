from django.db import models


class Denek(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    text = models.TextField()
    is_valid = models.BooleanField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True,blank=True,null=True)
    image = models.ImageField(upload_to="2023",null=True,blank=True)




    def __str__(self):
        return self.email