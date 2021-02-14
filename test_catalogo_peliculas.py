from dominio.peliculas import Pelicula
from servicios.catalogo_peliculas import CatalogoPeliculas

opcion = None
while(opcion != 4 ):
        print("Opciones", "\n")
        print("1- Agregar pelicula")
        print("2- Listar peliculas")
        print("3- Eliminar todo ")
        print("4- Salir")
        opcion = int(input("Escriba la opcion que desea realizar (1-4): " ))
       
        if(opcion == 1):
            nueva_pelicula = input("Proporcione el nombre:" )
            pelicula  = Pelicula(nueva_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif(opcion == 2): 
            CatalogoPeliculas.listar_peliculas()
        elif(opcion == 3):
            CatalogoPeliculas.eliminar_peliculas()
else:
        print("Cerra el programa capo")

