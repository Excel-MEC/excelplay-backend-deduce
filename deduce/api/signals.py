from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import CurrentLevel, Hint

from api.utils.firebase import firebase_current_level_ref, firebase_new_hint_ref


@receiver(post_save, sender=CurrentLevel)
def update_firebase_current_level(sender, instance, **kwargs):
    """This functions update current level in firebase realtime-db.
    As the production environment doesn't support socket, this is a workaround to notify the client."""

    # Update firebase db child
    ref = firebase_current_level_ref()
    ref.set({"level": instance.level, "user": instance.user})


@receiver(post_save, sender=Hint)
def update_firebase_new_hint(sender, instance, **kwargs):
    ref = firebase_new_hint_ref()
    ref.set({"level": instance.level.level_number, "hint": instance.hint})
