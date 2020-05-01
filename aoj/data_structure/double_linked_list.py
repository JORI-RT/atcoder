from functools import reduce


def to_str(x, y):
    return x + " " + y


class DoublyLinkedList:
    def __init__(self, data=[]):
        self.data = data

    def insert(self, x):
        self.data.insert(0, x)

    def delete(self, x):
        if self.data.count(x) > 0:
            self.data.remove(x)

    def delete_first(self):
        self.data = self.data[1:]

    def delete_last(self):
        self.data = self.data[:len(self.data) - 1]

    def show(self):
        print(reduce(to_str, self.data))


N = int(input())
dll = DoublyLinkedList()
for i in range(N):
    string = input()
    command = ""
    x = ""
    if string in "deleteFirst" or string in "deleteLast":
        command = string
    else:
        command, x = string.split()
    if command == 'insert':
        dll.insert(x)
    elif command == 'delete':
        dll.delete(x)
    elif command == 'deleteFirst':
        dll.delete_first()
    elif command == 'deleteLast':
        dll.delete_last()

dll.show()
