# Implement a Python function to determine if a singly linked list is a palindrome. You can't use additional data structures; solve it in O(n) time and O(1) space
# Determining whether a singly linked list is a palindrome with O(n) time complexity and O(1) space complexity can be done through the following steps:

# 1. Find the middle of the linked list.
# 2. Reverse the second half of the linked list.
# 3. Compare the first half and the second half.
# 4. Reverse the second half back to its original state (Optional, if you want to keep the linked list as it was).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):
    # Step 1: Find the middle of the linked list
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    while slow is not None:
        nextTemp = slow.next
        slow.next = prev
        prev = slow
        slow = nextTemp

    # Step 3: Compare the two halves
    first_half = head
    second_half = prev
    is_palindrome = True
    while second_half is not None:
        if first_half.data != second_half.data:
            is_palindrome = False
            break
        first_half = first_half.next
        second_half = second_half.next

    # Step 4: Reverse the second half back (optional)
    prev = None
    while second_half is not None:
        nextTemp = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = nextTemp

    return is_palindrome

# Test the function
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

result = isPalindrome(head)
print("Is palindrome:", result)  # Output should be True

# This function first finds the middle of the list and reverses the second half. Then it compares the first and second halves to see if they are the same, thus determining whether the list is a palindrome. If you want to preserve the original linked list, you can add a fourth step to reverse the second half back to its original state. The function achieves this in O(n) time complexity and O(1) space complexity.