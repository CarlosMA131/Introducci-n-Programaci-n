# def EscribirCentrado(texto):
#     cal= 40 /2
#     x = texto.center(cal)
#     print(x)
#     return x
# EscribirCentrado(texto="hola")



# def max_in_list():
#     lista_numeros=[ 1,7,234,9,13,56,4,23,678,456 ]
    
#     return max(lista_numeros)
# print(max_in_list())

# def mas_larga():
#     palabras = input("Dime varias palabras:")
#     contar = palabras.split()
#     larga=contar[0]
#     for n in contar:
#         if len(n) > len(contar):
#             larga = n
#     return larga

# print(mas_larga())


# def filtrar_palabras():
#     palabras = input("Dime una lista de palabras: ").split()
#     entero = int(input("Dime un entero: "))

#     for palabra in palabras:
#         if len(palabra) >= entero:
#             print(palabra)

# filtrar_palabras()

# def masy():
    # mayusculas=input("Dime una cadena:")
    # resutado=[]
    # for c in mayusculas: 
        # resutado.append(c.isupper())
    # return resutado.count(True)
# print("Las Este nuemro de letras en mayusculas",masy())
# 

def cal_datos():
    anyo_curos=int(input("Dime que año se cursa: "))
    person=0
    while person < 3:
        personas=[]
        nom=input("Dime el nombre de la person: ")
        edad=input("Dime el año de nacimiento: ")
        ingre=person.append(nom)
        anyo=person.append(edad)
        return print (personas)

print(cal_datos())