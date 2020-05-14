from apscheduler.schedulers.background import BackgroundScheduler

from api.models import CurrentLevel
from api.utils.firebase import firebase_current_level_ref


def update_current_level_job():
    level = CurrentLevel.objects.first().level
    user = CurrentLevel.objects.first().user
    ref = firebase_current_level_ref()
    ref.set({"level": level, "user": user})


def job_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_current_level_job, 'interval', minutes=5)
    scheduler.start()
