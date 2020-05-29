from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

""""
O Scan varre toda a tabela, filtra os itens selecionados e discarta os outros dados.

"""

def scan_movies(year_range, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")

    table = dynamodb.Table('Movies')
    scan_kwargs = {
        # Especifica a condição
        # 'FilterExpression': (6) Key('year').between(*year_range),
        # Especifica os campos que serão retornados
        'ProjectionExpression': "#yr, title, info.rating",
        # Faz a substituição de nome, pois year é reservado no dynamo
        'ExpressionAttributeNames': {"#yr": "year"},
        'Limit': 5
    }

    """
        O Scan retorna um subconjunto de itens por vez, chamados páginas.
        O valor LastEvaluatedKey na resposta é passado para o método scan por
        meio do parâmetro ExclusiveStartKey. Quando a última página é retornada,
        LastEvaluatedKey não é parte da resposta.
    """
    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        display_movies(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    def print_movies(movies):
        for movie in movies:

            print(f"\n{movie['year']} : {movie['title']}")
            print(movie)
            # pprint(movie['info'])

    query_range = (1950, 1959)
    print(f"Scanning for movies released from {query_range[0]} to {query_range[1]}...")
    scan_movies(query_range, print_movies)

#
# quando nao tem nada filtrado -> faz scan
# quando é contato -> query
# quando é produto, com contato -> query
# quando é
# quando é produto, sem contato -> scan