movies = {"Avengers: Infinity War":"PG-13 - Con supervision de padres"
,"Tortugas Ninja: Caos Mutante":"PG - Para todas las edades"
,"Frozen":"PG - Para todas las edades"
,"It":"R - Restringida"}
while(True):
    print("Escribe la palabra salir para terminar con la ejecucion del programa\n")

    for key in movies:
        print("* "+key)

    inputMovie=input("\nIngresa el nombre de alguna de las peliculas para saber su clasificacion:\n")

    if(inputMovie=="salir"):
        break

    movie = movies.get(inputMovie)

    if(movie == None):
        print("La pelicula no existe por favor ingresa otra pelicula\n ")
    else:
        print("La clasificacion de la pelicula: " + inputMovie + " es: "+movie+"\n")

