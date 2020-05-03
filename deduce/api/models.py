from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    """Custom User model."""

    id = models.CharField(max_length=50, primary_key=True)
    profile_picture = models.URLField(null=False, blank=False)
    # DEPRECIATED - not being used since all users are always on the same level
    level = models.IntegerField(default=1, null=False)
    last_anstime = models.DateTimeField(null=True)
    score = models.IntegerField(default=0, null=False)

    def get_full_name(self):
        return super().get_full_name()

    def __str__(self):
        return "{} | {}".format(self.get_full_name(), self.email)

    class Meta:
        ordering = ["-level", "last_anstime"]

    def create_refresh_token(self):
        """Create refresh_token for the given user instance."""
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class Level(models.Model):
    options = (("I", "Image"), ("NI", "Not Image"))
    level_number = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=200, null=False)
    question = models.TextField(null=True)

    level_file_1 = models.FileField(upload_to="level_images/", null=True, blank=True)
    level_file_2 = models.FileField(upload_to="level_images/", null=True, blank=True)
    level_file_3 = models.FileField(upload_to="level_images/", null=True, blank=True)

    cover_image = models.FileField(upload_to="cover_images/", null=False, blank=False)
    is_locked = models.BooleanField(default=True)
    unlocked_by = models.ForeignKey(
        User,
        related_name="unlocked_by",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.level_number)


class CurrentLevel(models.Model):
    level = models.IntegerField(default=1)


class Hint(models.Model):
    level = models.ForeignKey(Level, related_name="hints", on_delete=models.CASCADE)
    hint = models.TextField()

    def __str__(self):
        return "Hint for {0}".format(self.level)


class AnswerLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    answer = models.TextField()
    anstime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%-30s| %10s | %10s | %10s " % (
            self.user,
            self.answer,
            self.level,
            self.anstime,
        )
