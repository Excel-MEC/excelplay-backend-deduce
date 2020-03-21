from django.contrib import admin
from .models import DeduceUser, Level, Hint, AnswerLog

admin.site.register(DeduceUser)
admin.site.register(Level)
admin.site.register(Hint)
admin.site.register(AnswerLog)
