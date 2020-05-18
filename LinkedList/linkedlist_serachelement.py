class Node:
    ''' Function to initialise the node object '''
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

    def search(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False

    ''' This function prints content of linked list starting from head '''
    def printlist(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

if __name__ == '__main__':
    LL = LinkedList()
    LL.push(1)
    LL.push(3)
    LL.push(7)
    LL.printlist()
    print(LL.search(1))
