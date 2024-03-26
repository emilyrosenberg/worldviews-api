from django.db import models
from django.contrib.auth.models import User
from plans.models import Plan


class PlanComment(models.Model):
    """
    PlanComment model, related to User and Plan
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
