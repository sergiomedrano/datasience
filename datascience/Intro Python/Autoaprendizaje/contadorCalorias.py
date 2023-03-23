import math

proteina = float(input("Ingrese los gr de proteínas:\n>"))
carbo = float(input("Ingrese los gr de carbohidratos:\n>"))
grasa = float(input("Ingrese los gr de grasa:\n>"))

calorias = 4*(proteina+carbo) + 9*grasa

print(f'Total calorías: {math.ceil(calorias)}')