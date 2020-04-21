from apscheduler.schedulers.background import BackgroundScheduler

from api.models import CurrentLevel
from api.utils.firebase import firebase_current_level_ref

def update_current_level_job():
    current_level = CurrentLevel.objects.first().level
    ref = firebase_current_level_ref()
    ref.set(current_level)

def job_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_current_level_job, 'interval', minutes=5)
    scheduler.start()
