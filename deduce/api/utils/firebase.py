import environ

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase Setup
env = environ.Env()
SERVICE_ACCOUNT = env.str("GOOGLE_APPLICATION_CREDENTIALS", "../key.json")
cred = credentials.Certificate(f"{SERVICE_ACCOUNT}")
firebase_admin.initialize_app(cred, {"databaseURL": "https://excelmec.firebaseio.com/"})


def firebase_current_level_ref():
    ref = db.reference("current_level")
    return ref


def firebase_new_hint_ref():
    ref = db.reference("new_hint")
    return ref
