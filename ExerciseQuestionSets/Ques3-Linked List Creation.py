# Implement a basic singly linked list class in Python. Include methods for appending nodes, inserting nodes at specific positions, and printing the linked list.
class Node:
    def __init__(self, data):
        self.data = data  # Holds the data of the node
        self.next = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    # Method to append a node to the end of the list
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode  # If list is empty, set new node as head
            return
        lastNode = self.head  # Start from the head
        while lastNode.next:  # Traverse to the end of the list
            lastNode = lastNode.next
        lastNode.next = newNode  # Set the next of last node to the new node

    # Method to insert a node at a specific position
    def insertAtPosition(self, position, data):
        # Validate position
        if position < 0:
            print("Position must be non-negative.")
            return
        
        newNode = Node(data)
        # Inserting at the beginning
        if position == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        currentNode = self.head
        count = 0
        # Traverse to the node just before the desired position
        while currentNode and count < position - 1:
            currentNode = currentNode.next
            count += 1
        
        # Validate if position is out of bounds
        if currentNode is None:
            print("Position out of bounds.")
            return
        
        newNode.next = currentNode.next
        currentNode.next = newNode

    # Method to print the list
    def printList(self):
        if self.head is None:
            print("List is empty.")
            return
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")

# Initialize and populate the linked list
myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)

# Print the list
print("After appending elements:")
myList.printList()  # Output: 1 -> 2 -> 3 -> None

# Insert an element at a specific position
myList.insertAtPosition(1, 4)

# Print the list again
print("After inserting element at position 1:")
myList.printList()  # Output: 1 -> 4 -> 2 -> 3 -> None

# Insert an element at an invalid position
myList.insertAtPosition(-1, 5)
myList.insertAtPosition(10, 6)

# Print the list again
print("After attempting invalid insertions:")
myList.printList()  # Output should remain: 1 -> 4 -> 2 -> 3 -> None
