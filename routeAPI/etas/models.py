from django.db import models

# Create your models here.
class ETAS(models.Model):
    eta_text = models.CharField(max_length=100, blank=True)
    start_text = models.CharField(max_length=100, blank=True)
    end_text = models.CharField(max_length=100, blank=True)
    time_text = models.CharField(max_length=100, blank=True)