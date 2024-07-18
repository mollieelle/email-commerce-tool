
from django.db import models

class EmailDraft(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    recipients = models.TextField()  # Store as comma-separated values

    def __str__(self):
        return self.subject
