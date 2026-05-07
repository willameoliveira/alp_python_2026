from math import sqrt

x1 = int(input("Digite x1: "))
x2 = int(input("Digite x2: "))
y1 = int(input("Digite y1: "))
y2 = int(input("Digite y2: "))

d = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distância dos pontos é de: {d:.2f}")