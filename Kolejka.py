class Kolejka:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)



k = Kolejka()
k.enqueue(1)
k.enqueue(2)
k.enqueue(3)
print(k.size())  # 3
print(k.peek())  # 1
print(k.dequeue())  # 1
print(k.dequeue())  # 2
print(k.dequeue())  # 3
print(k.dequeue())  # None



#__init__: konstruktor, tworzy pustą listę, która będzie reprezentować kolejkę
#is_empty: sprawdza, czy kolejka jest pusta
#enqueue: dodaje nowy element do kolejki
#dequeue: usuwa i zwraca pierwszy element kolejki, jeśli kolejka nie jest pusta; w przeciwnym razie zwraca None
#peek: zwraca pierwszy element kolejki, jeśli kolejka nie jest pusta; w przeciwnym razie zwraca None
#size: zwraca liczbę elementów w kolejce