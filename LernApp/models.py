from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class LernKarte(models.Model):
    name = models.CharField(max_length=50)
    tag = models.ForeignKey('LernApp.Tag', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey('LernApp.Project', on_delete=models.CASCADE)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('lernkarte_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
