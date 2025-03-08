"""
valor y referencia
"""

#tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
#my_int_b = 20
#my_int_a = 30
print(my_int_a)
print(my_int_b)

#tipos de datps ṕr referemcia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

#funciones como datos por valor




def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

# funciones con datos por referencia



def my_list_func(my_list: list):
    my_list.append(30)
    print(my_list)

my_list_c = [10, 20 ]
my_list_func(my_list_c)
print(my_list_c)
