# Corrected ListNode class
class ListNode:
    def __init__(self, value=0, next=None):  # Corrected here
        self.value = value
        self.next = next

# Function to merge two sorted lists
def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.value < l2.value:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def linkedListToList(head):
    lst = []
    while head:
        lst.append(head.value)
        head = head.next
    return lst

# Create two sorted linked lists
l1 = createLinkedList([1, 2, 4])
l2 = createLinkedList([1, 3, 4])

# Merge the two lists
merged_list = mergeTwoLists(l1, l2)

# Convert the merged linked list back to a Python list to display it
merged_list_as_list = linkedListToList(merged_list)
print(merged_list_as_list)
