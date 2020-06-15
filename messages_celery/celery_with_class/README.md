### Para rodar o projeto em celery

- Criar virtualenv 
- script path: apontando para bin/celery da virtualenv 
- Em parameters:
worker
-A
messages_celery.celery_with_class.app.app
-l
info
-P
gevent
-n
tasks-worker@%n
--autoscale=1,1
-Q
tasks

Worker directory apontando para a pasta.



from celery import current_app


print("Enviando mensagem!")
current_app.send_task("first-task", args=[], kwargs= {'message': 'Welcome!!'}, queue='tasks')
print("Mensagem enviada!")


