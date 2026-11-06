# Sistema sencillo de gestión de pedidos en una cafetería

menu = {
    "café": 1.2,
    "té": 1.0,
    "sandwich": 3.5,
    "croissant": 2.0
}

carrito = []

print("=== Bienvenido a la cafetería digital ===")
print("Menú disponible:")
for producto, precio in menu.items():
    print(producto.capitalize(),precio,"€")

while True:
    pedido = input("\n¿Qué deseas pedir? (escribe 'fin' para terminar): ").lower()
    if pedido == "fin":
        break
    elif pedido in menu:
        cantidad = int(input(f"¿Cuántos {pedido}s quieres?: "))
        carrito.append({"producto": pedido, "cantidad": cantidad, "precio": menu[pedido]})
    else:
        print("Ese producto no está en el menú.")

# Cálculo del total (Aquí hay un pequeño error intencionado en el cálculo)
total = 0
for item in carrito:
    subtotal = item["cantidad"] * item["precio"]
    print(f"{item['cantidad']} x {item['producto']} → {subtotal} €")
    total += subtotal 

print("\nTotal a pagar:", total, "€")
