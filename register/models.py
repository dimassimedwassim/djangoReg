from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name