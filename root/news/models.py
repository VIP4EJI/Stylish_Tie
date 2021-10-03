from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    about = models.CharField(max_length=256, null=False)
    picture = models.FileField(upload_to='pictures/', blank=True, null=True)
    date_created = models.TimeField(auto_now_add=True, null=False)
    source = models.URLField(null=False)

    def __str__(self) -> str:
        return str(self.title)
