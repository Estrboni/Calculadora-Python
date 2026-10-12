# 🧮 Calculadora Básica en Python

## Descripción
Este proyecto es una calculadora básica desarrollada en Python que permite realizar operaciones matemáticas fundamentales: suma, resta, multiplicación y división.

## Características
- Suma de dos números
- Resta de dos números
- Multiplicación de dos números
- División con manejo de errores (división por cero)
- Interfaz de menú interactivo por consola

## Requisitos
- Python 3.6 o superior

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU-USUARIO/proyecto-calculadora.git

#programador2

## 🧩 Arquitectura Modular (Programador 3)

En esta fase se implementó una **estructura modular** para desacoplar la lógica de entrada de datos y la visualización de resultados, aplicando principios de código limpio y separación de responsabilidades.

### Nuevas Funciones Incorporadas:
- **`obtener_datos()`**: Encargada de capturar los valores numéricos ingresados por el usuario de forma independiente.
- **`mostrar_todos_los_resultados(a, b)`**: Centraliza la ejecución simultánea de todas las operaciones aritméticas básicas y muestra el reporte completo en consola.

### 💻 Ejemplo de Implementación del Módulo:
```python
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