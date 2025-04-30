class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data {key} not found.")
            return

        prev.next = current.next
        current = None

# User Input
ll = LinkedList()
n = int(input("Enter number of nodes to insert: "))
for _ in range(n):
    data = int(input("Enter node data: "))
    ll.insert(data)

ll.display()

delete_key = int(input("Enter data to delete: "))
ll.delete(delete_key)
ll.display()
