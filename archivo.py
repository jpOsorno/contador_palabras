import os
import re

class Archivo:
  def __init__(self, ruta):
    self.ruta = ruta
    self.nombre = os.path.basename(ruta)
    self.extension = os.path.splitext(ruta)[1].lower()

  def contar_palabra(self, palabra):
    total_palabras = 0
    with open(self.ruta, 'r') as archivo:
      texto = archivo.read().lower()
      patron = re.compile(r"(?<!\w){}(?!\w)".format(palabra))
      total_palabra = len(patron.findall(texto))
    return total_palabra