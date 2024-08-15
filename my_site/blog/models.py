from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return self.full_name()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.caption}"