import BadArray

maxSize = 10                                  # Tamaño máximo del arreglo
arr = BadArray.Array(maxSize)                 # Crear el objeto Array
 
arr.insert(77)                                # Insertar 10 elementos
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)
 
print("Array contiene", arr.nItems, "elementos")
arr.traverse()
 
print("Buscar 12 devuelve", arr.search(12))
print("Buscar 12.34 devuelve", arr.search(12.34))
 
print("Eliminar 0 devuelve", arr.delete(0))
print("Eliminar 17 devuelve", arr.delete(17))
 
print("Array después de eliminar tiene", arr.nItems, "elementos")
arr.traverse()
