class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def getCountRec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    def getCount(self):
        return self.getCountRec(self.head)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
print 'Count of nodes is :',llist.getCount()
print('Created list :')
llist.printList()
