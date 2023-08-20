# Stack list example
stackList = [1, 2, 3, 4, 5, 6, 7, 8]

# Add an element to the stack (Push operation)
def stackAddElement(element):
    stackList.append(element)

# Retrieve the top element from the stack (Retrieve operation)
def stackRetrieveElement():
    item = stackList[len(stackList) - 1]
    stackList.pop()
    return item

# Search for and delete an element from the stack
def searchAndDeleteElement(element):
    tempStack = []
    
    while not isEmpty():
        current_element = stackRetrieveElement()
        if current_element == element:
            print("Element", element, "removed from the stack")
            break
        else:
            tempStack.append(current_element)
    
    while tempStack:
        stackAddElement(tempStack.pop())

# Check if the stack is empty
def isEmpty():
    return len(stackList) == 0

# Usage of all functions
stackAddElement(9)
print("Stack after push:", stackList)

print("Retrieve element:", stackRetrieveElement())

searchAndDeleteElement(5)
print("Stack after search and delete:", stackList)
