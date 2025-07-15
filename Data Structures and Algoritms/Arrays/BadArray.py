# Implementar una estructura de datos Array como un tipo simplificado de lista.

class Array(object):
 
   def __init__(self, initialSize):          # Constructor
      self.__a = [None] * initialSize        # El arreglo se almacena como una lista
      self.nItems = 0                        # No hay elementos al inicio
 
   def insert(self, item):                   # Insertar elemento al final
      self.__a[self.nItems] = item           # El elemento va al final actual
      self.nItems += 1                       # Aumentar el contador de elementos
 
   def search(self, item):                   # Buscar un elemento
      for j in range(self.nItems):           # Buscar entre los elementos actuales
         if self.__a[j] == item:             # Si se encuentra
            return self.__a[j]               # Devolver el elemento
      return None                            # Si no se encuentra, devolver None
 
   def delete(self, item):                   # Eliminar la primera ocurrencia
      for j in range(self.nItems):           # del elemento
         if self.__a[j] == item:             # Si se encuentra el elemento
            for k in range(j, self.nItems):  # Mover los elementos a la izquierda
               self.__a[k] = self.__a[k+1]
            self.nItems -= 1                 # Reducir el número de elementos
            return True                      # Devolver indicador de éxito
      return False                           # Si no se encuentra, devolver False
 
   def traverse(self, function=print):       # Recorrer todos los elementos
      for j in range(self.nItems):           # y aplicar una función
         function(self.__a[j])
