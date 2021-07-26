from DataStructures.SinglyLinkedList import SLLIterative


class TableNode:
    def __init__(self, data):
        self.data = data
        self.list = SLLIterative.SLL_I()

    def getList(self):
        return self.list

    def getData(self):
        return self.data

    def setData(self, value):
        self.data=value



