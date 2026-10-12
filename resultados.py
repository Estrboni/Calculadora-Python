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
mostrar_todos_los_resultados(num1, num2)