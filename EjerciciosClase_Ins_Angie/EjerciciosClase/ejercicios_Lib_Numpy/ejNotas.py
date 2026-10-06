import numpy as np

estudiantes = np.array([
    [5.0, 3.2, 4.0],
    [3.0, 4.5, 3.5],
    [2.5, 3.4, 4.8],
    [3.8, 5.0, 4.3],
])

print(estudiantes.shape)

print(estudiantes.mean(axis=0))
print(estudiantes.mean(axis=1))

