import csv
import time
bucle=True
Inventario=[]
precio=[]
code=[]
si=True
def VerP():
    Nom_Archivo="ListaProductos.txt"
    with open(Nom_Archivo,"w") as file:
        file.write("--producto--    ---Precio---    ---código---\n")
        for i in Inventario:
            file.write(f"-.{i}          {precio}          {code} \n")
    print(f"Se ha creado un archivo llamado: {Nom_Archivo} en su sistema...")
    time.sleep(2)
def eliminarP():
    try:
        elim = input("Ingrese el producto que desea eliminar: ")
    except ValueError:
        print("Ha ocurrido un error")
    Inventario.remove(elim)
    print("\n***El producto se ha elimindado correctamente***\n")
    time.sleep(2)
    pass
def modificarP():
    try:
        producmod = input("Ingrese el producto que desea modificar: ")
    except ValueError:
        print("Ha ocurrido un error")
    if producmod in Inventario:
        Inventario.remove(producmod)
        Inventario.append(producmod)
def agregarP():
    while True:
        print("--> Agregar producto al inventario o salir para volver al menú <--\n")
        try:
            produc=input()
        except ValueError:
            print("Se ha encontrado con un error...")
            time.sleep(2)
        if produc in Inventario:
            print("¡Error el producto ya se encuentra en el inventario...!")
            time.sleep(2)
        elif produc=='salir':
            print(" ")
            break
        else:
            Inventario.append(produc)
            try:
                preciow=int(input("Ingresa el precio: \n--> "))
                precio.append(preciow)
                codew=int(input("Ingresa el código: \n--> "))
                code.append(codew)
            except ValueError:
                print("A ocurrido un problema al agregar producto...")
                time.sleep(2)
            print("Se ha agregado correctamente ")

            time.sleep(2)
            False
        print(f"Lista de productos: {Inventario}")
while bucle == True:
    print("     ******MENÚ******\n1. Agregar un producto.\n2. Ver todo los productos.\n3. Modificar un producto.\n4. Eliminar un producto.\n5. Guardar colección en un archivo.\n6. Salir del programa.\n")
    opcion=input("Seleccione una opcion digitando su numero: \n")
    if opcion == "1":
        agregarP()
        si=True
    elif opcion == "2":
        print(f"Lista de productos: {Inventario}")
    elif opcion == "3":
        modificarP()
    elif opcion == "4":
        eliminarP()
    elif opcion == "5":
        VerP()
    elif opcion == "6":
        print("Saliendo del programa...")
        time.sleep(2)
        bucle = False