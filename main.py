import numpy as np
import csv

"""
Instrucciones:
1. Pasar listas a arreglo numpy //
2. Como operar en arreglo numpy
3. Como trabajar con CSVs // 
4. Operaciones aritmeticas y de difusion
5. Acceso a arreglos numpy

a. Mostrar caso 
b. Que datos requiere para abordarlo
c. Donde se obtuvo datos
d. Formula (funcion) para operarlos
e. Explicar resultados
"""

# variable para la direccion del archivo csv
csv_path = 'healthcare-dataset-stroke-data.csv'

# Abrir y leer el archivo csv
file = open(csv_path,newline='')
reader = csv.reader(file)

# Guardar datos del csv en una lista 
data = list(reader)

# Convertir la lista de listas 'data' en arreglo numpy
csv_array = np.array(data)

#Slicing para obtener edad (2), hypertension(3), heart_disease(4), avg_glucose (8), bmi (9), stroke (11)

csv_slices = csv_array[:,[2,3,4,8,9,11]]

# Quitar todas las filas con valores 'N/A' en bmi 

csv_slices = csv_slices[csv_slices[:,4] != 'N/A']
print(csv_slices[0])
# Operacion aritmetica
# Hacer todos los valores float a excepcion de la primera fila (header)
valores = csv_slices[1:,:].astype(float)

print(csv_slices)

stroke = valores[:,-1]

# Obtener promedio de cada columna
Avg = np.mean(valores, axis=0)

#Obtener maximo de cada columna
max_values = np.max(valores, axis=0)

#Obtener peso
weights = np.round((Avg / max_values)* 100)
print("\nWeights:\n",weights)

