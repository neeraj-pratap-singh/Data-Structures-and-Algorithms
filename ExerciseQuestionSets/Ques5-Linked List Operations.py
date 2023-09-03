# Write a Python function to reverse a singly linked list in-place. Provide both iterative and recursive solutions.
# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class definition
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append a node to the list
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    # Method to print the linked list
    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")

    # Method to reverse the list iteratively
    def reverseIteratively(self):
        prevNode = None
        currentNode = self.head
        while currentNode:
            nextNode = currentNode.next  # Store next node
            currentNode.next = prevNode  # Reverse the current node
            prevNode = currentNode  # Move prevNode one step ahead
            currentNode = nextNode  # Move currentNode one step ahead
        self.head = prevNode  # Reset head to the last node in the list

    # Utility method for recursive reversal
    def reverseRecursivelyUtil(self, currentNode, prevNode):
        if not currentNode:
            self.head = prevNode
            return
        nextNode = currentNode.next
        currentNode.next = prevNode
        self.reverseRecursivelyUtil(nextNode, currentNode)

    # Method to reverse the list recursively
    def reverseRecursively(self):
        self.reverseRecursivelyUtil(self.head, None)


# Initialize and populate the linked list
myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)

# Print the original list
print("Original List:")
myList.printList()  # Output: 1 -> 2 -> 3 -> None

# Reverse the list iteratively and print it
myList.reverseIteratively()
print("List after iterative reversal:")
myList.printList()  # Output: 3 -> 2 -> 1 -> None

# Reverse the list recursively and print it
myList.reverseRecursively()
print("List after recursive reversal:")
myList.printList()  # Output: 1 -> 2 -> 3 -> None
