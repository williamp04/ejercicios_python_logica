"""
ejercicio
"""
#pila/stack (LIFO)

#push
stack = []
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

#pop
stack_item = stack[len(stack) -1]
del stack[len(stack) -1]
print(stack_item)

print(stack.pop())

print(stack)
#cola/queue (fifo)

queue = []

#enqueue
queue.append(1)
queue.append(2)
queue.append(3)

#dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)


"""
extra
"""

# web

def web_navigation():

    stack = []

    while True:

        action = input(
            "Añade una url o interactua con las palabras claves adelante/atras/salir: "
        )

        if action == "salir":
            print("saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}")

        else:
            print("estas en la pagina de inicio de la web")


#web_navigation()

def shared_printed():

    queue = []

    while True:

        action = input("añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len (queue) > 0:
                print(f"imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"cola de impresion: {queue}")


shared_printed()