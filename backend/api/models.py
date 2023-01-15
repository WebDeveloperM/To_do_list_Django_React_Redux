from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False, blank=True, null=True)
    slug = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.title
