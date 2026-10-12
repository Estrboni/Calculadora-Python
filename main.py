def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))
print("Multiplicacion:", multiplicar(num1, num2))
print("Division:", dividir(num1, num2))
