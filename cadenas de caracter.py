"""
operaciones
"""

s1 = "hola"
s2 = "python"

# concatenacion

print(s1 + ", " + s2 + "!")

#repeticion

print(s1 * 3)

# indexacion

print(s1[0] + s1[1] + s1[2] )

#longitud

print(len(s2))

#slocing (porcion)

print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

#busqueda
print("ho" in s1)
print("i" in s1)

# reemplazo

print(s1.replace("o", "a"))

#dividir
print(s2.split("t"))

#Mayusculas y minusculas y primera letra en mayuscula
print(s1.upper())
print(s1.lower())
print("william pinto".title())
print("william pinto".capitalize())


# eliminar espacios
print("william pinto ".strip() + "@williamp04")

#busqueda al princiio y al final
print(s1.startswith("ho"))
print(s1.startswith("py"))
print(s1.endswith("la"))
print(s1.endswith("on"))

s3 = "alex pinto @williamp04"
#busqueda de posicion
print("alex pinto @williamp04".find("william"))
print("alex pinto @williamp04".find("alex"))
print("alex pinto @williamp04".find("w"))
print("alex pinto @williamp04".lower().find("a"))

#busqueda de ocurrencias

print(s3.lower().find("william"))

#formateo

print("saludo: {}, lenguaje: {}!".format(s1,s2))

#interpolacion
print(f"saludo: {s1}, lenguaje: {s2}!")

#transformacion en lista de caracteres
print(list(s3))

#transformacion de lista en cadena

l1 =[s1, ", ", s2, "!"]
print("".join(l1))

#trandformaciones numericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.789"
s5 = float(s5)
print(s5)

#comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


"""
extra
"""

def check(word1, word2: str):

    #palindromos
    print(f"¡{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¡{word2} es un palindromo?: {word2 == word2[::-1]}")

    #anagrama
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")
    print(sorted(word1) == sorted(word2))

    #isograma 
    print(f"¿{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un isograma?: {len(word2) == len(set(word2))}")

    def isograma(word:str) -> bool:

        word_dict = dict()
        for word in word2:
            word_dict[word] = word_dict.get(word, 0) + 1


        isograma = True
        values = list(word_dict.values())
        isograma_len = values[0]
        for word_count in values:
            if word_count != isograma_len:
                isograma = False
                break

        return isograma

    print(f"{word1} es un isograma?: {isograma(word1)}")
    print(f"{word2} es un isograma?: {isograma(word2)}")


check("radar", "pythonpythonpythonpython")
#check("amor", "roma")







