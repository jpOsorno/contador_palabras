import os
from carpeta import Carpeta

def main():
  ruta_carpeta = input('Introduzca la ruta de la carpeta: ')
  palabra = input('Introduzca la palabra a buscar: ')


  if os.path.exists(ruta_carpeta):
    carpeta = Carpeta(ruta_carpeta)
    if(carpeta.cargar_archivos()): 

      total_palabras = carpeta.buscar_palabra(palabra)

      print('Cantidad de la palabra "{}" en cada archivo:'.format(palabra))
      for archivo, total in total_palabras.items():
        print('  {}: {}'.format(archivo, total))

      total_carpeta = sum(total_palabras.values())
      print('Cantidad total en la carpeta: {}'.format(total_carpeta))
    else: 
      print("No se encontraron archivos de texto en la carpeta")
  else: 
    print("La carpeta no existe en el sistema")

  

if __name__ == '__main__':
  main()