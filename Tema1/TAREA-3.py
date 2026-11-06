# estudiante = {}
# nom=input("Dime el nombre del estudiante: ")
# es=input("Dime el nombre de la asignatura: ")
# nota=input("Dime la nota: ")


# estudiante["Nombre"]= nom
# estudiante["Asignatura"]= es
# estudiante["Nota"]= nota

# print(estudiante)

# clav=input("Dime una clave ")

# if clav.lower() == "nombre":
#     print(estudiante["Nombre"])
# elif clav.lower() == "asignatura":
#     print(estudiante["Asignatura"])
# elif clav.lower() == "nota":
#     print(estudiante["Nota"])
# else:
#     print("tus muertos")

# Actividad 2  
# pr=0
# cesta={"pan": 0.80, "leche": 1.20, "manzanas": 2.50, "huevos": 2.10}
# for a,b in cesta.items():
#     print("Articulo: ",a," Precio: ",b,"€")
#     pr=pr+b
# print("Coste Total:",pr)

# Actividad 3
stock= {"tornillos": 100, "tuercas": 150, "arandelas": 200}
print(stock)
pd=input("Dime el nombre del producto: ")
ct=int(input("Dime la cantidad de producto: "))

stock[pd]=ct
# actualiza y suma 
if pd in stock:
    stock[pd]+=ct
else:
    stock[pd]=ct
print(stock)

con=input("Dime un articulo para cosultar su stock: ")
if con in stock :
    print("Este es el stock del articulo",stock.get(con))
