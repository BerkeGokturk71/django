from django.db import models
from ckeditor.fields import RichTextField


class Category (models.Model):
    topic = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50,null=True,unique=True)
    def __str__(self):
        return self.topic
class Tag (models.Model):
    topic = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50,null=True,unique=True)
    def __str__(self):
        return self.topic
class Post (models.Model):
    topic = models.CharField(max_length=10,help_text="konu baslıgı",unique=True)
    text_area = RichTextField()
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag,blank=True,null=True)
    image = models.ImageField(upload_to="blog/%Y/%m/%d/")
    date = models.DateTimeField(auto_now=True)
    is_avaible = models.BooleanField(default=True)

    def __str__(self):
        return self.topic


