class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    nextNode = None
    
    while current:
        nextNode = current.next  # Save the next node
        current.next = prev      # Reverse the current node's pointer
        prev = current           # Move prev to current
        current = nextNode       # Move to the next node
    
    return prev  # prev is the new head of the reversed list

# Example Usage:
# Creating a linked list 1->2->3->4->None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Reversing the linked list
reversed_list_head = reverse_linked_list(head)

# Helper function to print the linked list
def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Print the reversed linked list
print_list(reversed_list_head)
