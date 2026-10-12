# Programador1 entrada de datos
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

#Programador2

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(operacion, a, b):
    operaciones = {
        "1": sumar,
        "2": restar,
        "3": multiplicar,
        "4": dividir
    }
    funcion_seleccionada = operaciones[operacion]
    return funcion_seleccionada(a, b)

print("1. Sumar | 2. Restar | 3. Multiplicar | 4. Dividir")
opcion = input("Elige una opcion (1-4): ")
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

print("Resultado:", calcular(opcion, num1, num2))

#programador3-salida de datos

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def obtener_datos():
    n1 = float(input("Primer numero: "))
    n2 = float(input("Segundo numero: "))
    return n1, n2

def mostrar_todos_los_resultados(a, b):
    print("Resultados:")
    print("-> Suma:", sumar(a, b))
    print("-> Resta:", restar(a, b))
    print("-> Multiplicacion:", multiplicar(a, b))
    print("-> Division:", dividir(a, b))

num1, num2 = obtener_datos()
mostrar_todos_los_resultados(num1, num2)ss