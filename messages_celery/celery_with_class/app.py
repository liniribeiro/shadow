from celery import Celery
from celery.signals import import_modules

from messages_celery.celery_with_class.tasks.first_task import FirstTask

app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')


# @signals.celeryd_after_setup.connect
# def database_migration(**kwargs):
#     migration.upgrade()

@import_modules.connect
def import_modules(*args, **kwargs):
    app.register_task(FirstTask())


