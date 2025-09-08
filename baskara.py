import math
print("calcular bascara")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))



delta = b**2 - 4*a*c

if delta  < 0: 
 print("inpossivel calcular no momento")
else:
 x2 = (-b - math.sqrt(delta)) / (2 * a)
 x1 = (-b + math.sqrt(delta)) / (2 * a)


print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Resultados:   " )
print("delta = ", delta)
print("x1 = ", x1)
print("x2 = ", x2)
