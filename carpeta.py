import os
from archivo import Archivo

class Carpeta:
  def __init__(self, ruta):
    self.ruta = ruta
    self.archivos = []

  def buscar_palabra(self, palabra):
    total = {}
    for archivo in self.archivos:
      total[archivo.nombre] = archivo.contar_palabra(palabra)
    return total

  def cargar_archivos(self):
    for archivo in os.listdir(self.ruta):
      ruta_archivo = os.path.join(self.ruta, archivo)
      if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()
        if extension in ('.txt', '.xml', '.json', '.csv'):
          self.archivos.append(Archivo(ruta_archivo))
          return True
        else: 
            return False