import requests
from string import Template
import json

apiKey="ab1ad77639ff09b837da76a4cc663d17"
urlSearch= Template('https://api.themoviedb.org/3/search/movie?query=$n1&api_key=$n2')

while(True):
    print("Si deseas salir solo escribe salir")
    palabra=input("Ingresa una palabra de la pelicula que quieres buscar\n\n")

    if(palabra=="salir"):
        break

    resultado =  requests.get(urlSearch.substitute(n1=palabra, n2=apiKey))
    payload=json.loads(resultado.text)

    if(len(payload['results'])>0):
        result = payload['results'][0]
        print("Titulo: "+ str(result['original_title']))
        print("Puntuacion: "+ str(result['vote_average']))
        print("\n")
    else:
        print("No se encontro informacion")

