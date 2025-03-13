"""
funciones definidas por el usuario
"""

#simple


def greet():
    print("hola python!")


greet()

# con retorno

def return_greet():
    return "hola python!"

print(return_greet())

# con un argumento

def arg_greet(name):
    print(f"hola {name}")

arg_greet("alex")

#con argumentos


def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("hola", "alex")

#con argumentos predeterminados

def default_args_greet(name= "python"):
    print(f"hola, {name}")

default_args_greet("alex")
default_args_greet()

# con argumentos y retorn


def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("hola", "alex"))

#con retorno de varios valores

def multiple_return_greet():
    return "hola", "python!"

greet, name = multiple_return_greet()
print(greet)
print(name)

# con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"hola, {name}!")

variable_arg_greet ("alex", "william", "python", "brais")

# con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"hola, {value} ({key})!")

variable_key_arg_greet(
    language="python",
    name="william",
    alias="alex",
    edad="36"
)

"""
funciones dentro de funciones
"""

def outer_funcion():
    def inner_funcion():
        print("funcion interna: hola python!")
    inner_funcion()

outer_funcion()

"""
funciones del lengaje (built-in)
"""

print(len("william pinto"))
print(type(36))
print("william".upper())

"""variables locales y globales """

global_variable = "python"

print(global_variable)

def hello_python():
    local_var= "hola"
    print(f"{local_var}, {global_variable}")

print(global_variable)
# print(local_var) no se puede acceder desde fuera de la funcion

hello_python()

"""
extra
"""

def print_numbers(text1,text2)-> int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("fizz", "buzz"))