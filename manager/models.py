from django.db import models

# Create your models here.


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/skill/')

    def __str__(self):
        return self.name


class About(models.Model):
    greetings = models.CharField(max_length=20, default='')
    about_quote = models.CharField(max_length=999)
    image = models.ImageField(upload_to='images/about/')

    def __str__(self):
        return self.greetings


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    category = models.CharField(max_length=50, default='')
    details = models.CharField(max_length=255)
    github_url = models.CharField(max_length=300, default='')
    image = models.ImageField(upload_to='images/projects')

    def __str__(self):
        return self.name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=350)

    def __str__(self):
        return self.name
