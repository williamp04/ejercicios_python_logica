import os

"""
Ejercicio
"""

file_name= "williamp04.txt"

with open(file_name, "w") as file:
    file.write("William Pinto\n")
    file.write("20 años\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""
Extra
"""

file_name= "williamp04_shop.txt"

open(file_name, "a")

while True:
    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3.Actualizar producto")
    print("4. Eliminar producto")
    print("5.mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por prodecto")
    print("8. Salir")

    option = input("Selecciona una opcion: ")
    #1. Añadir Producto
    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
    #2. Consultar Producto
    elif option == "2":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    #3. Actualizar producto
    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    #4. Eliminar producto
    elif option == "4":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    #5. Mostrar productos
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    #6. Calcular venta total
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(",")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(f"Venta total: {total}")
    #7. Calcular venta por producto
    elif option == "7":
        name = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(",")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(f"Venta total: {total}")
    #8. Salir
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("selecciona una de las opciones disponibles.")