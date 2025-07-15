# --------------------------------------------
# 🧠 Introducción a los arrays en Python
# --------------------------------------------

# En Python, los "arrays" se llaman listas (list)
# Son colecciones ordenadas, modificables y dinámicas.

# --------------------------------------------
# ✅ 1. Crear un array con valores fijos
# --------------------------------------------
lecturas = [10, 20, 30, 40]
print("📦 Array original:", lecturas)

# --------------------------------------------
# ✅ 2. Acceder a elementos del array
# --------------------------------------------
print("🎯 Primer valor (índice 0):", lecturas[0])
print("🎯 Último valor (índice -1):", lecturas[-1])

# --------------------------------------------
# ✅ 3. Modificar un valor del array
# --------------------------------------------
lecturas[1] = 25  # Cambiamos el segundo valor
print("✏️ Modificamos el segundo valor:", lecturas)

# --------------------------------------------
# ✅ 4. Agregar elementos (array dinámico)
# --------------------------------------------
lecturas.append(50)  # Agrega al final
print("➕ Agregado al final:", lecturas)

lecturas.insert(1, 15)  # Inserta en la posición 1
print("📌 Insertado en posición 1:", lecturas)

# --------------------------------------------
# ✅ 5. Eliminar elementos
# --------------------------------------------
lecturas.remove(30)  # Elimina el primer 30 que encuentre
print("❌ Eliminamos el 30:", lecturas)

valor_eliminado = lecturas.pop(2)  # Elimina por índice
print("🗑️ Eliminado por índice 2:", valor_eliminado)
print("Array después del pop:", lecturas)

# --------------------------------------------
# ✅ 6. Recorrer el array
# --------------------------------------------
print("🔁 Recorriendo el array:")
for lectura in lecturas:
    print(" -", lectura)

# --------------------------------------------
# ✅ 7. Tamaño y ordenamiento
# --------------------------------------------
print("📏 Tamaño del array:", len(lecturas))
lecturas.sort()  # Ordena de menor a mayor
print("⬆️ Ordenado:", lecturas)

# --------------------------------------------
# ✅ 8. Borrar todo el array
# --------------------------------------------
lecturas.clear()
print("🚫 Array vacío:", lecturas)

# --------------------------------------------
# ✅ 9. Crear un array dinámico desde cero
# --------------------------------------------
print("\n===============================")
print("🌡️  Simulación de lecturas dinámicas")
print("===============================\n")

# Importamos módulo para tiempo
import time

# Creamos un array vacío
lecturas_dinamicas = []

# Usamos un bucle para simular lecturas cada 5 segundos
for i in range(3):  # Puedes cambiar 3 por el número de lecturas que desees
    valor = int(input(f"Ingrese lectura {i+1}: "))
    momento = time.strftime("%H:%M:%S")  # Hora actual en formato legible
    lectura = {
        "tiempo": momento,
        "valor": valor
    }
    lecturas_dinamicas.append(lectura)
    print(f"✅ Lectura registrada: {lectura}")
    time.sleep(5)  # Espera 5 segundos (puedes quitar esto en pruebas)

# Mostramos el array final
print("\n📊 Lecturas almacenadas:")
for lectura in lecturas_dinamicas:
    print(f" - {lectura['tiempo']}: {lectura['valor']}")

# Fin del script 🎉
