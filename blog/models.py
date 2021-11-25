from django.db import models
from django.core.validators import EmailValidator, MinValueValidator , MaxValueValidator , MinLengthValidator
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    




class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL ,null=True, related_name="posts")
    exerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True , default="",blank=True ,null=False, db_index=True) 
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)








