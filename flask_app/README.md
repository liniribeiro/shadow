
Comandos para gerar uma nova imagem e enviar para o dockerhub:
 - docker image build -t aliniribeiroo/shadow:latest .  
 - docker push aliniribeiroo/shadow 

Comandos para rodar o projeto com docker-compose:
 - docker-compose up
 
 
 
 ### Para rodar o projeto em celery

- Criar virtualenv 
- script path: apontando para bin/gunicorn da virtualenv 
- Em parameters:
-c ./src/gunicorn.py src.app:app

Worker directory apontando para a pasta.




