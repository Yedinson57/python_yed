import numpy as np

ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])
aumento = ventas * (10 / 100)
ventas_aumento = ventas + aumento

print(f"ventas: {ventas}")
print(f"ventas con un aumento del 10%: {ventas_aumento}")
