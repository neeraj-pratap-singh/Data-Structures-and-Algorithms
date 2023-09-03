# Write a Python function that finds the intersection point of two singly linked lists. If the lists do not intersect, return None. Optimize for time and space complexity
# To find the intersection point of two singly linked lists, you can use the following optimized approach that has a time complexity of \(O(N + M)\), where \(N\) and \(M\) are the lengths of the two linked lists, and a constant additional space complexity \(O(1)\).

# Here's how the algorithm works:

# 1. Calculate the lengths of both linked lists.
# 2. Find the length difference between the two lists, say \(d\).
# 3. Move the head pointer of the longer list \(d\) steps forward.
# 4. Now traverse both lists simultaneously until you either find the intersection point or reach the end of the lists.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to get the length of a linked list
def getLength(head):
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next
    return length

# Function to find intersection point
def findIntersection(head1, head2):
    len1, len2 = getLength(head1), getLength(head2)
    
    # Move the head pointer of the longer list 'd' steps ahead
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next
    
    # Traverse both lists simultaneously to find the intersection point
    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1, head2 = head1.next, head2.next
    
    return None

# Sample linked lists
# List 1: 1 -> 2 -> 3 -> 4
# List 2:      5 -> 3 -> 4
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)

head2 = Node(5)
head2.next = head1.next.next  # 3

# Test the function
print(findIntersection(head1, head2))  # Output should be 3

# In this example, we have two linked lists that intersect at node with data `3`. The `findIntersection` function correctly identifies this node as the intersection point.