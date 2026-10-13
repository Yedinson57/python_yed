import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])

desviacion_std = np.std(notas)

print(notas.mean(axis = 0)) 
print(notas.shape) 
print(desviacion_std)
print(notas.max()) 
print(notas.min()) 