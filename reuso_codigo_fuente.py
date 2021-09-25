# Vamos a ver como a través del uso de funciones podemos evitar tener código fuente repetido
# Código fuente aportado por Walter Grachot (tiene unos 34 sentencias originalmente)
def carga_producto_y_calcula_subtotal():
    producto= input("Ingrese nombre del producto comprado: ")
    valor= float(input("Ingrese su valor: "))
    cantidad= int(input("Ingrese la cantidad: "))
    total= (valor*cantidad)
    producto = (producto, valor, cantidad)
    print(total)
    print()
    return total, producto

def imprimir_subtotales(producto):
    print("Compró " + str(producto[1][2]) + " " + str(producto[1][0]) + " a un Precio Unitario de $" + str(producto[1][1]) + " por un total de " + str(producto[0]))

print("Bienvenido al Supermercado Don Erne")
print("-" * 80)
dato_producto1 = carga_producto_y_calcula_subtotal()
dato_producto2 = carga_producto_y_calcula_subtotal()
dato_producto3 = carga_producto_y_calcula_subtotal()
dato_producto4 = carga_producto_y_calcula_subtotal()

imprimir_subtotales(dato_producto1)
imprimir_subtotales(dato_producto2)
imprimir_subtotales(dato_producto3)
imprimir_subtotales(dato_producto4)

total_general = dato_producto1[0] + dato_producto2[0] + dato_producto3[0] +dato_producto4[0]
print ("Ha gastado en total " + str(total_general)) 

