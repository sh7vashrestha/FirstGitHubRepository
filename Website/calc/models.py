from django.db import models

class Todo(models.Model):
    work = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.work