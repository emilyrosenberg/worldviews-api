from django.db import models


class Location(models.Model):
    """
    Location model, related to posts and plans
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.name}"
