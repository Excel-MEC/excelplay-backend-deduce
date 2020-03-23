from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    profile_picture = models.URLField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)
