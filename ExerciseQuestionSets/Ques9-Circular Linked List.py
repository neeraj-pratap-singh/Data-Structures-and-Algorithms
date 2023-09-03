# Create a Python class for a circular linked list and include methods for insertion, deletion, and traversal. Demonstrate how to add elements to and remove elements from a circular linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Insert at specific position
    def insertAtPosition(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node
            return

        temp = self.head
        count = 0
        while temp:
            if count == position - 1:
                new_node.next = temp.next
                temp.next = new_node
                if new_node.next == self.head:
                    return
            temp = temp.next
            count += 1
            if temp == self.head:
                break

    # Delete a node by value
    def delete(self, key):
        if self.head:
            if self.head.data == key:
                # Check if there is only one node in the list
                if self.head.next == self.head:
                    self.head = None
                    return
                # Delete the head node
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
                return
            
            # Delete non-head node
            prev = None
            temp = self.head
            while temp.next != self.head:
                prev = temp
                temp = temp.next
                if temp.data == key:
                    prev.next = temp.next
                    return

    # Print the circular linked list
    def display(self):
        nodes = []
        temp = self.head
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(map(str, nodes)))

# Create a circular linked list and append elements
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)

# Display the list
print("Circular Linked List after appending elements:")
cll.display()  # Output should be 1 -> 2 -> 3 -> 4 -> 5

# Insert an element at position 2
cll.insertAtPosition(3, 2)
print("Circular Linked List after inserting 3 at position 2:")
cll.display()  # Output should be 1 -> 2 -> 3 -> 4 -> 5

# Insert an element at position 0
cll.insertAtPosition(0, 0)
print("Circular Linked List after inserting 0 at position 0:")
cll.display()  # Output should be 0 -> 1 -> 2 -> 3 -> 4 -> 5

# Insert an element at the last position
cll.insertAtPosition(6, 6)
print("Circular Linked List after inserting 6 at the last position:")
cll.display()  # Output should be 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Delete an element
cll.delete(3)
print("Circular Linked List after deleting element with value 3:")
cll.display()  # Output should be 1 -> 2 -> 4 -> 5

# Delete the head element
cll.delete(1)
print("Circular Linked List after deleting head element:")
cll.display()  # Output should be 2 -> 4 -> 5

# Delete an element that doesn't exist
cll.delete(9)
print("Circular Linked List after trying to delete an element that doesn't exist:")
cll.display()  # Output should still be 2 -> 4 -> 5
