# uso de return vs uso de print en funciones
def suma_return(a, b):
    return a + b

def suma_print(a, b):
    print(a + b)    


a = suma_return(2, 5)
print(a) # Debería imprimir 7 (que es el valor de a)

b= suma_print(2, 5)
print(b) # Debería imprimir 7 (que es el valor de b)
