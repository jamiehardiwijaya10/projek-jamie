import numpy as np

suhu = np.array([30, 32, 28, 35, 31, 29, 33, 34, 27, 36])
suhu_fahrenheit = (suhu * 9/5) + 32

print(f"Suhu awal (Celcius): {suhu}")
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit}")