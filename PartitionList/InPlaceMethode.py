class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def partition(head, x):
    # Initialize 'before' and 'after' pointers
    before = before_head = ListNode(0)
    after = after_head = ListNode(0)

    # Traverse the original linked list
    current = head
    while current:
        # If the current node's value is less than 'x', move it to the 'before' partition
        if current.value < x:
            before.next = current
            before = before.next
        else:
            # Move 'current' to the 'after' partition
            after.next = current
            after = after.next
        # Move 'current' to the next node
        current = current.next

    # Link the tail of the 'before' partition to the head of the 'after' partition
    before.next = after_head.next
    # End the 'after' partition
    after.next = None

    # Return the modified linked list starting from the 'before' partition
    return before_head.next

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