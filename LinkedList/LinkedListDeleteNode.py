# Python program to delete a node from linked list

class Node:
    #Counstructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Constuctor to initialize the head
    def __init__(self):
        self.head = None

    #Function to insert new node at the beginning
    def push (self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #delete the first occurence of the key in the LinkedList
    def deleteNode(self, key):
        # store head Node
        temp = self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key was not present in the linked List
        if (temp == None):
            return
        # unlike the node from linked List
        prev.next = temp.next

        temp = None

    # Utility function to print the linked List
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


#Drive program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("created list is : ")
llist.printList()
llist.deleteNode(1)
print ("\nLinked List after Deletion of 1:")
llist.printList()
