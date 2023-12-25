class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def partition(head, x):
    # Initialize 'dummy' nodes for the two partitions
    dummy1 = ListNode(0)
    dummy2 = ListNode(0)
    current1, current2 = dummy1, dummy2

    # Traverse the original linked list
    current = head
    while current:
        # If the current node's value is less than 'x', append it to the first partition
        if current.value < x:
            current1.next = current
            current1 = current1.next
        else:
            # Append the current node to the second partition
            current2.next = current
            current2 = current2.next
        # Move 'current' to the next node
        current = current.next
    
    # Link the tail of the first partition to the head of the second partition
    current1.next = dummy2.next
    # End the second partition
    current2.next = None

    # Return the modified linked list
    return dummy1.next

# Example usage:
# Constructing the linked list
# 1 -> 4 -> 3 -> 2 -> 5 -> 2, and x = 3
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

# Applying the partition function
new_head = partition(head, 3)

# Printing the partitioned list
current = new_head
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next