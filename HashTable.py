from DataStructures.HashTable import HashTableNode
import random

def hash_function(size, data):
    return data%size

class HT:
    def __init__(self, size):
        self.size = size
        self.collision = 0
        self.table = []

        counter = 0
        while(counter<size):
            self.table.append(HashTableNode.TableNode("$")) # $ represents an empty node
            counter+=1

    def insert(self, value):
        position = hash_function(self.size, value)
        if self.table[position].getData() == "$":
            self.table[position].setData(value)
        else:
            self.collision+=1
            listInNode = self.table[position].getList()
            listInNode.InsertAtEndIterative(value)

    def printo(self):
        counter = 0
        for node in self.table:

            print(counter, end="| ", flush=True)
            print(node.getData(), end=" ", flush=True)
            if not(node.getList().isEmpty()):
                node.getList().printListIterative()
            else:
                print("")
            counter+=1


if __name__ == '__main__':
    h = HT(100)
    for x in range(100):
        h.insert(random.randint(0, 1000))
    h.printo()



