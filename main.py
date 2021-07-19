#librería para leer el teclado
from readchar import readchar
#imprimir la cabecera
print('''
Para comenzar oprima cualquier tecla
Categorías:
(1) Aseo
(2) Otros
(0) Totalizar
***************************************************************
''')
#se inicializa la variable
suma_aseo = 0 

while True:
    precio = int(input("Por favor ingrese el precio del artículo o totalice (0): "))
    if precio != 0:
        cat= int(input("Categoría Aseo(1) Otros(2) ")) #variable auxiliar, para capturar el input como entero.
        if cat == 1:
            suma_aseo = suma_aseo + precio
            continue
        else:
            print("No es  un artículo de aseo")
            continue
    else:
        print("Subtotal:  ", suma_aseo)
        print("¿Continuar? Si(s) No (n)")
        rc = readchar() #variable que guarda la lectura del teclado como caracter
        if rc == "s":
            print(rc)
            continue
        elif rc == "n":
            print(rc)
            break
        else:
            precio = 0
            continue

print("El total de su compra es: ", suma_aseo, "\nGracias por preferirnos")

