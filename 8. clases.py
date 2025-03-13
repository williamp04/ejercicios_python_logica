"""
ejercicio
"""

class Programmer:

    surname:str = None

    def __init__(self, name: str, age: int, languages: list) -> None:
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(f"nombre: {self.name} |Apellidos:{self.surname} | edad: {self.age} | lenguajes: {self.languages}")

my_programmer = Programmer("Alex", 21, ["python", "javascript", "typescript"])
my_programmer.print()
my_programmer.surname = "pinto"
my_programmer.print()
my_programmer.age = 37
my_programmer.print()

"""
extra
"""
#LIFO



class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for intem in reversed(self.stack):
            print(intem)

my_stack = stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

#FIFO

class queue:
    def __init__(self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)

    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)
            

    def print(self):
        for item in reversed(self.queue):
            print(item)

my_queue = queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
my_queue.count()
print(my_queue.count())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
