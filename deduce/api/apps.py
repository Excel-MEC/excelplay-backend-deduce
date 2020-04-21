from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals  # noqa
        from api.utils.cron_job import job_scheduler # noqa
        job_scheduler()