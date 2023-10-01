print("soy my helper")
print("dime numeros para hacer una lista")
lista = list(((input())))
print(lista)


print("Quieres agregar datos a tu lista")
si_no = input()
def agregar_datos():
    lista.append(input())
    print(lista)
     
if si_no == "si":
    agregar_datos()
else:
    print("Bueno tengo otra que te va ayudar")

print("Ahora quieres revisar si hay un numero")
si_no = input()

def obtener_datos():
    respuesta = input()
    if respuesta in lista:
        print("si tu elemento esta en la lista") 
    else:
        print("no, no esta el elemento")


if si_no == "si":
    obtener_datos()