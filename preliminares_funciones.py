# funciones en mate
# definición de la funcion
# f(x) = x +10
# f1(x) = -1*x**2 + 4*x +30

# uso de la funcion o el calculo de la misma
# f(0) = 0 + 10 = 10
# f(1) = 1 + 10 = 11
# Puedo graficarla haciendo y=f(x)

def f(x):
    return x + 10

def f1(x):
    return -1*x**2 + 4*x + 30

# indentation o sangria o tabulado
def saludar(texto):
    return "Hola, " + texto

def clave(nombre, apellido, anio):
    valor = nombre[0] + apellido[0] + "_" + str(anio)
    return valor

a = 0
print(f(0))
print(f(1))

print(f1(7))
print(f1(8))

a = saludar("Felipe")
print(a)

n = input("Ingrese el nombre: ")
a = input("Ingrese el apellido: ")
an = int(input("Ingrese el año: "))
print(clave(n, a, an))

