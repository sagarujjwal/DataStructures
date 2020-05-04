
# Node class
class Node:
    #Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assisgn data
        self.next = None # initialize next as null

# Linked list class contains  a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    #This function prints content of linked list starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

# Code execution starts from here

if __name__ == '__main__':

    #starts with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next=second
    second.next=third
    llist.printList()
