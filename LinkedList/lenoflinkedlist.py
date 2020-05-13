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

    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            temp=temp.next
            count+=1
        print("Lenght of LinkedList is : {}".format(count))

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
llist.getCount()
print('Created Linked list is :')
llist.printList()
