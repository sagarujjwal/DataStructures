#class queue to represent a queue
class Queue:
    def __init__(self,capacity):
        self.front = self.size=0
        self.rear = capacity -1
        self.Q = [None]*capacity
        self.capacity = capacity

    #Queue is full when size becomes equal to the capacity
    def isFull(self):
        return self.size == self.capacity
    #Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0
    #Function to add an item to the queue. It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print('Full')
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s Enqueue to Queue" %str(item))

    #Funtion to remove an item from queue. It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return
        print(" %s Dequeue from the queue" %str(self.Q[self.front]))
        self.front = (self.front +1) % (self.capacity)
        self.size = self.size - 1

    #Funtion to get front of Queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        print("Front item is ", self.Q[self.front])

    #Funtion to get rear of Queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Rear item is ", self.Q[self.rear])


#Driver Code
if __name__ == '__main__':
    print('__name__', __name__)
    queue = Queue(10)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
    print(queue.Q)
