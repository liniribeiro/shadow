import csv
import random

import names
from faker import Faker

modules = ['git', 'introdução ao python', 'scrum', 'banco de dados', 'aprofundamento ao python', 'github', 'carreiras']
periods = ['matutino', 'vespertino', 'noturno']
turma = ['1', '2', '3']

with open("curso.csv", "a") as file:
    headers = ["nome", "cpf", "uf", "turma", "data_nascimento", "email", "endereco", "período", "modulo"]
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")

    writer.writeheader()
    faker = Faker('pt-BR')
    x = 0
    while x < 500:
        faker_name = faker.name()
        name = faker_name.replace("Dr. ", "").replace("Sr. ", "").replace("Sra. ", "").replace("Srta. ", "").replace("Dra. ", "")
        writer.writerow({
            'nome': name,
            'cpf': faker.cpf(),
            'uf': faker.state(),
            'endereco': faker.street_address(),
            'turma': random.choice(turma),
            'data_nascimento': faker.date_between(start_date='-30y', end_date='-15y'),
            'email': faker.email(),
            'período': random.choice(periods),
            'modulo': random.choice(modules),
        })
        x+=1
