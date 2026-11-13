# # def tabla(numero):
    
# #     print("TABLA DE MULTIPLICAR DEL Nº:",numero)
# #     for i in range(1, 11) :
# #         print(f"{numero} x {i} = {numero * i}")

# # numero=int(input("Dame un numero entero del 1 al 10: "))

# # if numero >= 1 and numero <= 10:   
# #     tabla(numero)
# # else:
# #     print("no esta dentro del rango")




# # 2 Validar Opciones

# # def valida_opcion():
# #     while True:
# #         print("="*32)
# #         print("   ","GAMIFICACIÓN EN EL AULA")
# #         print("="*32)
# #         print("""
# #         1 - Cargar Datos del fichero
# #         2 - Imprimir datos
# #         3 - Jugar
# #         4 - Guardar Datos
# #         5 - Cambiar contraseña
# #         0 - SALIR """)
# #         print("-"*32)

# #         opcion = int(input("Dame la Opción: "))
# #         return opcion


# # opcion=valida_opcion()

# # if opcion <= 0 and opcion >= 5:
# #         print("Porfavor, vuelve a intentarlo")

# # while True :
# #     if opcion == 0: 
# #         print("Saliendo del programa")
# #         break
# #     elif opcion in range(0,6):
# #         print("La opcion seleccionada es: ",opcion)
# #     else :
# #        print("Porfavor, vuelve a intentarlo")
    
# #     opcion=valida_opcion()








# def lista_jugadores():
#     print("*"*32)
#     print(" ","JUGADORES ON-LINE")
#     print("*"*32)
#     print(""" 
#     1 - Llega un jugador nuevo
#     2 - Se va un jugador
#     3 - FIN""")
#     print("-"*32)
#     opcion=int(input("Dame la opción: "))
#     return opcion

# jugadores = ["mario","mafalda","luigi","esther","heidi","songoku","beauty","beast"]

# while True:
   
#     opcion=lista_jugadores()

#     if opcion == 3:
#         print(jugadores)
#         break
#     elif opcion == 1 :
#         anya=input("¿Quien eres?")    
#         jugadores.append(anya)
#         print(f"Bienvenid@ jugador {anya}")
#         for jugador in jugadores:
#             print(jugador, end=" - ")
#     elif opcion == 2:
#         jugadores.pop(0)
#         for jugador in jugadores:
#             print(jugador, end=" - ")
#     else :
#         print("Error en la opcion, introduce una correcta")
