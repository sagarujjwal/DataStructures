#Node class
class Node:
    # FUnction to initialize the node object
    def __init__(self, data):
        self.data = data   # Assisgn the data
        self.next = None   # initialize next as Null

#Linked List class
class LinkedList:
    # Function to initialize the LinkedList object
    def __init__(self):
        self.head = None

    # Function to insert a new node at beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node & put in the data
        new_node = Node(new_data)

        # 3. Make next of new node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # Insert a new node after the given prev_node
    def insertAfter(self, prev_node, new_data):

        # 1. check if the given prev_node exists
        if prev_node is None:
            print "The given previous node must inLinkedList."
            return

        #  2. create new node &
        #      Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    #Append a new node at the end
    def append(self, new_data):

        # 1. create a new Node
        # 2. put in the data
        # 3. set next as None
        new_node = Node(new_data)

        # 4. If LinkedList is empty, then make the new node as head.
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next

        # 6. change the next of last node
        last.next =new_node

    # Utility function to print the linked List
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp=temp.next

# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    llist.insertAfter(llist.head.next.next.next, 5)

    print 'Created linked list is:',
    llist.printList()
