# Create a Python function to detect if a given linked list contains a cycle. Implement Floyd's Tortoise and Hare algorithm to solve this problem efficiently.
### Floyd's Tortoise and Hare Algorithm

# Floyd's Tortoise and Hare algorithm, also known as the cycle detection algorithm, is an efficient way to determine if a linked list has a cycle or loop. The algorithm uses two pointers, one moving at a slower pace (the Tortoise) and the other moving faster (the Hare). Initially, both pointers are set at the head of the list.

# The Hare moves two steps at a time while the Tortoise moves one step. If there is a cycle, the Hare will eventually "lap" the Tortoise and the two pointers will meet at some point. If the Hare reaches the end of the list (`None`), it means the list is acyclic.

# ### What Does it Mean for a Linked List to Contain a Cycle?

# In a linked list, a cycle or loop occurs when a node points back to a previously traversed node, forming an endless loop. Normally, the last node in a linked list points to `None`, indicating the end of the list. But if any node points back to a node that has already been visited, it creates a cycle.

# Here's a graphical representation:

# - **Acyclic List**: 1 -> 2 -> 3 -> 4 -> 5 -> None
# - **Cyclic List**:  1 -> 2 -> 3 -> 4 -> 5 -> 2 (Node 5 points back to Node 2)

### Python Function to Detect Cycle using Floyd's Tortoise and Hare Algorithm

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def hasCycle(self):
        # Initialize Tortoise and Hare pointers to the head of the list
        tortoise = self.head
        hare = self.head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next  # Move the Tortoise one step
            hare = hare.next.next  # Move the Hare two steps

            # If Tortoise and Hare meet, a cycle is present
            if tortoise == hare:
                return True
        
        # If Hare reaches the end of the list, it is acyclic
        return False

# Test the function
myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

# Creating a cycle for testing: Node 4 points back to Node 2
myList.head.next.next.next.next = myList.head.next

# Check if the linked list has a cycle
print(myList.hasCycle())  # Output should be True

# This Python code defines a `LinkedList` class with a `hasCycle` method, which uses Floyd's Tortoise and Hare algorithm to detect if the list contains a cycle. The code includes a test to validate the function.