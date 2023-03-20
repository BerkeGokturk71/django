from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    message = models.TextField()


    def __str__(self):
        return self.email