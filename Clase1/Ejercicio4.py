import math 

print("Área de un circulo")
x = float(input("Ingrese el diametro: "))
radio = x/2
area = (math.pi * (radio * radio))  
print(f"El área es igual a: {area}")