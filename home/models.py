from django.db import models
from django.core.validators import validate_image_file_extension

class HomePosts(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Home-Images',validators=[validate_image_file_extension])
    link=models.URLField(blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-time']

class Gallery(models.Model):
    image= models.ImageField(upload_to='Gallery',validators=[validate_image_file_extension])
    text=models.CharField(max_length=40)
    uploaded_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-uploaded_on']

#class Video(models.Model):


class Tour(models.Model):
    text=models.CharField(max_length=50,unique=True)
    city=models.CharField(max_length=50)
    datetime=models.DateField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-datetime']

class Presskit(models.Model):
    genre=models.CharField(max_length=50)
    years_active=models.CharField(max_length=50)
    origin=models.CharField(max_length=50)
    bio=models.TextField()
    #presski=models.FileField
    image=models.ImageField(upload_to='Presskit',validators=[validate_image_file_extension])

    def __str__(self):
        return f"About-PressKit"

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-contacted_on']