from datetime import datetime

from celery.app.task import BaseTask


class FirstTask(BaseTask):
    name = "first-task"
    ignore_result = True

    def run(self, *args, **kwargs):
        today = datetime.now()
        print(kwargs['message'])

    def on_success(self, retval, task_id, args, kwargs):
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass
