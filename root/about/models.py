from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100, null=False)
    about = models.CharField(max_length=256, null=False)
    service = models.CharField(max_length=256, null=False)

    def __str__(self) -> str:
        return str(self.title)
