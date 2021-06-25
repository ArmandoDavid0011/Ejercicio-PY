# Ejercicio 4 Descuento de una compra.

print("---------Mercado Central------------")
precio=float(input("Compra total: $"))
print("----------------------------------------")
print("Compra se le aplicara un descuento ")
descuento=float(input("Aplicar descuento: "))
resultado = (precio *descuento)
print("***********************************************")
print(f"Gasto total: ${resultado:.2f}")
print("***********************************************")
