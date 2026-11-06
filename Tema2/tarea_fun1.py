# def tabla(numero):
    
#     print("TABLA DE MULTIPLICAR DEL Nº:",numero)
#     for i in range(1, 11) :
#         print(f"{numero} x {i} = {numero * i}")

# numero=int(input("Dame un numero entero del 1 al 10: "))

# if numero >= 1 and numero <= 10:   
#     tabla(numero)
# else:
#     print("no esta dentro del rango")




# 2 Validar Opciones

# def valida_opcion():
#     while True:
#         print("="*32)
#         print("   ","GAMIFICACIÓN EN EL AULA")
#         print("="*32)
#         print("""
#         1 - Cargar Datos del fichero
#         2 - Imprimir datos
#         3 - Jugar
#         4 - Guardar Datos
#         5 - Cambiar contraseña
#         0 - SALIR """)
#         print("-"*32)

#         opcion = int(input("Dame la Opción: "))
#         return opcion


# opcion=valida_opcion()

# if opcion <= 0 and opcion >= 5:
#         print("Porfavor, vuelve a intentarlo")

# while True :
#     if opcion == 0: 
#         print("Saliendo del programa")
#         break
#     elif opcion in range(0,6):
#         print("La opcion seleccionada es: ",opcion)
#     else :
#        print("Porfavor, vuelve a intentarlo")
    
#     opcion=valida_opcion()


def lista_jugadores():
    jugadores = ["mario","mafalda","luigi","esther","heidi","songoku","beauty","beast"]
    print(jugadores)
    print("*"*32)
    print(" ","JUGADORES ON-LINE")
    print("*"*32)
    print(""" 
    1 - Llega un jugador nuevo
    2 - Se va un jugador
    3 - FIN""")
    print("-"*32)
    opcion=int(input("Dame la opción: "))
    return opcion
    
opcion=lista_jugadores()

if opcion == 1 :
    anya=input("¿Quien eres?")    
    opcion=jugadores.put(anya)
    print(f"Bienvenid@ jugador {anya}")
    print("LISTA DE JUGADORES:",jugadores)

# import queue

# q = queue.Queue()

# q.put("Tarea 1")
# q.put("Tarea 2")
# q.put("Tarea 3")

# while not q.empty():
#     print(q.get())