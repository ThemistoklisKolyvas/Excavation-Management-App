from django.db import models
from django.contrib.auth.models import User

class Excavation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ditch_number = models.CharField(max_length=100)
    pottery = models.BooleanField(default=False)
    jewellery = models.BooleanField(default=False)
    bones = models.BooleanField(default=False)
    tools = models.BooleanField(default=False)
    small_findings = models.BooleanField(default=False)
    samples = models.BooleanField(default=False)
    east_dimension = models.FloatField()
    north_dimension = models.FloatField()
    depth = models.FloatField()
    graves_found = models.BooleanField(default=False)

    def __str__(self):
        return f"Excavation {self.ditch_number} by {self.user.username}"

class Grave(models.Model):
    excavation = models.ForeignKey(Excavation, related_name='graves', on_delete=models.CASCADE)
    grave_number = models.CharField(max_length=100, unique=True)
    comments = models.TextField()
    east_dimension = models.FloatField()
    north_dimension = models.FloatField()
    depth = models.FloatField()

    def __str__(self):
        return f"Grave {self.grave_number} in excavation {self.excavation.ditch_number}"

