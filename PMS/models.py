from django.db import models

# Create your models here.
class Project(models.Model):
    project_Name = models.CharField(max_length=200)
    uploaded_By = models.CharField(max_length=200)
    date = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.project_Name}-{self.uploaded_By}-{self.date}'
