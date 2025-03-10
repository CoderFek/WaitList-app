from django.db import models

# Create your models here.
class WaitListEntry(models.Model):
    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "WaitListEntries"

    def __str__(self):
        return self.email