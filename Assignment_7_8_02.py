class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    def display(self):
        return self.queue

# User Input
q = Queue()
n = int(input("Enter number of elements to enqueue: "))
for _ in range(n):
    item = int(input("Enter item to enqueue: "))
    q.enqueue(item)

print("Queue:", q.display())
dequeued_item = q.dequeue()
print("Dequeued item:", dequeued_item)
