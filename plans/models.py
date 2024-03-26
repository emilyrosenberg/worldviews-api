from django.db import models
from django.contrib.auth.models import User
from locations.models import Location


class Plan(models.Model):
    """
    Plan model, related to 'owner', i.e. a User instance, and location.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        default="1"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
