# Let's redefine the TreeNode class and implement the flatten function using recursive pre-order traversal.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flatten(root):
    # Define a helper function that takes the current node and the "previous" node
    # from the flattened list as parameters
    def flatten_helper(node, prev_node):
        if not node:
            return prev_node

        # Since it's pre-order, process the current node before its children
        prev_node.right = node
        prev_node.left = None
        prev_node = node

        # Temporarily store the right child because it will be overwritten
        right_child = node.right

        # Recursively flatten the left subtree and update the previous node
        prev_node = flatten_helper(node.left, prev_node)
        # Recursively flatten the right subtree and update the previous node
        prev_node = flatten_helper(right_child, prev_node)

        return prev_node

    # Dummy node to provide an easy start to the "previous" pointer
    dummy = TreeNode(-1)
    flatten_helper(root, dummy)

# Construct the tree again for demonstration
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Flatten the tree
flatten(root)

# Function to print the flattened tree
def print_flattened_tree(node):
    while node:
        print(node.val, end=' -> ' if node.right else '')
        node = node.right
    print()

# Test the function and print the flattened tree
print("The flattened binary tree using recursive pre-order traversal:")
print_flattened_tree(root.right)  # We start from root's right child due to the dummy node we used.
