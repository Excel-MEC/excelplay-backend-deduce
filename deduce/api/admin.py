from django.contrib import admin
from .models import User, Level, Hint, AnswerLog, CurrentLevel

admin.site.register(User)
admin.site.register(Level)
admin.site.register(Hint)
admin.site.register(AnswerLog)
admin.site.register(CurrentLevel)
