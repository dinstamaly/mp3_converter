from django.db import models


class Music(models.Model):
    url = models.URLField(max_length=250)
    email = models.EmailField(max_length=250)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email