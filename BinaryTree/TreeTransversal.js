class Node {
    constructor(val) {
        this.val = val;
        this.leftChild = null;
        this.rightChild = null;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert(val) {
        let newNode = new Node(val);
        if (this.root === null) {
            this.root = newNode;
        } else {
            this.insertNode(this.root, newNode);
        }
    }

    insertNode(node, newNode) {
        if (newNode.val < node.val) {
            if (node.leftChild === null) {
                node.leftChild = newNode;
            } else {
                this.insertNode(node.leftChild, newNode);
            }
        } else {
            if (node.rightChild === null) {
                node.rightChild = newNode;
            } else {
                this.insertNode(node.rightChild, newNode);
            }
        }
    }

    inorderTransversal(node) {
        if (node !== null) {
            this.inorderTransversal(node.leftChild);
            console.log(node.val);
            this.inorderTransversal(node.rightChild);
        }
    }

    preorderTransversal(node) {
        if (node !== null) {
            console.log(node.val);
            this.preorderTransversal(node.leftChild);
            this.preorderTransversal(node.rightChild);
        }
    }

    postorderTransversal(node) {
        if (node !== null) {
            this.postorderTransversal(node.leftChild);
            this.postorderTransversal(node.rightChild);
            console.log(node.val);
        }
    }
}

// Example Usage
const tree = new BinaryTree();
tree.insert(15);
tree.insert(25);
tree.insert(10);
tree.insert(7);
tree.insert(22);
tree.insert(17);
tree.insert(13);

console.log("inorderTransversal traversal:");
tree.inorderTransversal(tree.root);

console.log("preorderTransversal traversal:");
tree.preorderTransversal(tree.root);

console.log("postorderTransversal traversal:");
tree.postorderTransversal(tree.root);
