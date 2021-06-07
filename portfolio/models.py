from django.db import models
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    b_date = models.DateField()
    occupation = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name