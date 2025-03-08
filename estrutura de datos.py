# listas
my_list = ["alex", "william", "brais", "black"]
print(my_list)
my_list.append("carlos") # insercion
print(my_list)
my_list.remove("william") # borrado
print(my_list)
print(my_list[1]) #acceso
my_list[1] = "carlos" #modificacion
print(my_list)
my_list.sort() #ordenacion
print(my_list)

# tuplas
my_tuple = ("alex", "pinto", "williamp04", "21")
print(my_tuple[1]) # acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print(type(my_tuple))

#sets

my_set = {"alex", "pinto", "williamp04", "21"}
print(my_set)
my_set.add("alexgonzalez@gamil.com") # insercion
my_set.add("alexgonzalez@gamil.com") 
print(my_set)
my_set.remove("williamp04") # borrado
print(my_set)
my_set = set(sorted(my_set)) # no se puede ordenar
print(type(my_set))

# diccionarios

my_dict: dict ={
    "name":"alex",
    "apellido":"pinto",
    "username":"williamp04",
    "age":"21"
}
my_dict["email"] = "alexgonzalez@gamil.com" # insercion
print(my_dict)
del my_dict["username"] # borrado
print(my_dict["name"]) # acceso
my_dict["age"] = "25"#actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))

"""
extra
"""

def my_agenda():

    agenda = {}
    def insert_contact():
        phone = input("introduce el numero de telefono: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 10:
            agenda[name] = phone
        else:
            print("debes introducir un numero de telefono con menos de 10 digitos")

    while True:

        print("")
        print("1- buscar contacto")
        print("2. insertar contacto")
        print("3. actuaizar contacto")
        print("4. eliminar contacto")
        print("5. salir")

        option = input("\nseleccione una opcion: ")

        match option:
            case "1":
                name = input("introduce el nombre del contacto: ")
                if name in agenda:
                    print(f" el numero de telefono de {name} es {agenda[name]}")
                else:
                    print(f"el contacno {name} no existe")
            case "2":
                name = input("introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact
                else:
                    print(f"el contacno {name} no existe")
            case "4":
                name = input("introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"el contacno {name} no existe")
            case "5":
                print("saliendo de la agenda.")
                break
            case _:
                print("opcion invalida, elege del 1 al 5")

my_agenda()

