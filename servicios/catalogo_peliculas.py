import os

class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__() + "\n")
            
        except Exception as e:
            print("Ocurrio un error  al agregar peliculas" , e)
            
        finally:
            archivo.close() 
        
    @staticmethod
    def listar_peliculas():
       try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Peliculas disponibles:" + "\n")
            print(archivo.read())
            
       except Exception as e:
           print("Ocurrio un error al listar peliculas", e)
        
       finally:
           archivo.close()
           
   
    @staticmethod
    def eliminar_peliculas():
      try:
           os.remove(CatalogoPeliculas.ruta_archivo)
           print("Se ha eliminado todo lo contenido en ", ruta_archivo)
      except Exception as e:
          print("Ocurrio un error al eliminar las peliculas :", e)
          
   