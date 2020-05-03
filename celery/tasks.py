from celery import Celery

# tasks -> Nome do módulo,
# utilizado para que o nome das tasks sejam criadas automaticamente,
# quando as tasks são definidas no man modulo.

app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='America/Sao_Paulo',
    enable_utc=True,
)


@app.task
def first_task():
    return "OK"


# Para executar a aplicação podemos utilizar o comando:  celery -A tasks worker --loglevel=info
# Para chamar nossa task:
# from tasks import first_task
# first_task.delay()
