# Queue list example
queueList = [1, 2, 3, 4, 5, 6, 7, 8]

# Enqueue an element to the queue
def addElement(element):
    queueList.append(element)

# Dequeue an element from the front of the queue
def retrieveElement():
    if not isEmpty():
        return queueList.pop(0)

# Search for and delete an element from the queue
def searchAndDeleteElement(element):
    tempQueue = []

    while not isEmpty():
        current_element = retrieveElement()
        if current_element == element:
            print("Element", element, "removed from the queue")
            break
        else:
            tempQueue.append(current_element)

    while tempQueue:
        addElement(tempQueue.pop(0))

# Check if the queue is empty
def isEmpty():
    return len(queueList) == 0

# Usage of all functions
addElement(9)
print("Queue after adding new element:", queueList)

print("retrieve element:", retrieveElement())

searchAndDeleteElement(5)
print("Queue after search and delete:", queueList)
