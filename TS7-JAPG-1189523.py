"""José Adndrés Puaque Guerra
Carné: 1189523
21/09/2023"""

print("José Andrés Puaque Guerra")

X= input("Ingrese un número del 1 al 10 ")
XNUM= int(X)
if XNUM<1 or XNUM>10:
    print("Número no válido, verificar entrada.")
else:
    for OP in range(0,10):
        print(XNUM,"X",(OP+1),"=", XNUM*(OP+1))

opcion=input("Escriba continuar para realizar más operaciones, escriba cancelar si desea cerrar el programa ")
while opcion== "continuar":
    X= input("Ingrese un número del 1 al 10 ")
    XNUM= int(X)
    if XNUM<1 or XNUM>10:
        print("Número no válido, verificar entrada.")
    else:
        for OP in range(0,10):
            print(XNUM,"X",(OP+1),"=", XNUM*(OP+1))
    opcion=input("Escriba continuar para realizar más operaciones, escriba cancelar si desea cerrar el programa ")
