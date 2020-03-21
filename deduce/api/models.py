from django.db import models


class DeduceUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    level = models.IntegerField(default=1, null=False)
    last_anstime = models.DateTimeField(null=True)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ["-level", "last_anstime"]
        verbose_name_plural = "Deduce Users"


class Level(models.Model):
    options = (("I", "Image"), ("NI", "Not Image"))

    level_number = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=200, null=False)
    question = models.TextField(null=True)
    level_file = models.FileField(upload_to="level_images/", null=True, blank=True)
    filetype = models.CharField(
        max_length=10, choices=options, default="Image", blank=True
    )

    def __str__(self):
        return str(self.level_number)


class Hint(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    hint = models.TextField()

    def __str__(self):
        return "Hint for {0}".format(self.level)


class AnswerLog(models.Model):
    user = models.ForeignKey(DeduceUser, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    answer = models.TextField()
    anstime = models.DateTimeField(null=True)

    def __str__(self):
        return "%-30s| %10s | %10s | %10s " % (
            self.user,
            self.answer,
            self.level,
            self.anstime,
        )
