from django.db import models
from django.core.validators import validate_image_file_extension
from PIL import Image


class HomeImageAbout(models.Model):
    poster_image=models.ImageField(upload_to='Home-Poster-Images',validators=[validate_image_file_extension])
    about=models.TextField()
    image=models.ImageField(upload_to='Home-About-Image',validators=[validate_image_file_extension])

    def __str__(self):
        return f"HomeImageAbout"

    class Meta:
        verbose_name_plural='HomeImageAbout'

class HomePosts(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Home-Images',validators=[validate_image_file_extension])
    link=models.URLField(blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        #if img.height > 300 or img.width > 300:
        new_img = (573, 574)
        img.thumbnail(new_img)
        img.save(self.image.path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='HomePosts'
        ordering = ['-time']

class Gallery(models.Model):
    image= models.ImageField(upload_to='Gallery',validators=[validate_image_file_extension])
    text=models.CharField(max_length=40)
    uploaded_on=models.DateTimeField(auto_now_add=True)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        #if img.height > 300 or img.width > 300:
        new_img = (573, 574)
        img.thumbnail(new_img)
        img.save(self.image.path)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name_plural='Gallery'   
        ordering = ['-uploaded_on']

title_choices = (
    ("Spotify","Spotify"),
    ("SoundCloud","SoundCloud"),
    ("Mixcloud","Mixcloud")
)

class Music(models.Model):
    title=models.CharField(max_length=50,choices=title_choices)
    music=models.URLField()
    uploaded_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['uploaded_on']

class Video(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    video=models.FileField(upload_to='Video-Files')
    uploaded_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-uploaded_on']

class Tour(models.Model):
    text=models.CharField(max_length=50,unique=True)
    city=models.CharField(max_length=50)
    datetime=models.DateField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural='Tour'
        ordering = ['-datetime']

class Presskit(models.Model):
    genre=models.CharField(max_length=50)
    years_active=models.CharField(max_length=50)
    origin=models.CharField(max_length=50)
    bio=models.TextField()
    presskit=models.FileField(blank=True,null=True)
    work_profile=models.FileField(blank=True,null=True)
    image=models.ImageField(upload_to='Presskit',validators=[validate_image_file_extension])

    def __str__(self):
        return f"About-PressKit"
    
    class Meta:
        verbose_name_plural='Presskit'

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