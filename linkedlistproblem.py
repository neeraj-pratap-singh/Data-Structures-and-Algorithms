# Define the Employee class to represent each employee node
class Employee:
    def __init__(self, employeeID, employeeName, employeeSalary):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.employeeSalary = employeeSalary
        self.next = None  # Initialize the next pointer to None

# Define a function to insert an employee into the sorted linked list
def insertEmployee(head, employeeID, employeeName, employeeSalary):
    # Create a new employee node
    newEmployee = Employee(employeeID, employeeName, employeeSalary)
   

    # If the linked list is empty or the new employee should be inserted at the beginning
    if not head or employeeID < head.employeeID:
        newEmployee.next = head
        return newEmployee
    
    # Traverse the linked list to find the appropriate position to insert the new employee
    current = head
    while current.next and current.next.employeeID < employeeID:
        current = current.next
   
    # If an employee with the same ID already exists, update their information
    if current.employeeID == employeeID:
        current.employeeName = employeeName
        current.employeeSalary = employeeSalary
    # Insert the new employee after the current node
    else:
        newEmployee.next = current.next
        current.next = newEmployee
    return head
    
      
# Helper function to print the sorted linked list
def printLinkedList(head):
    current = head
    while current:
        print(f"ID: {current.employeeID}, Name: {current.employeeName}, Salary: {current.employeeSalary}")
        current = current.next

# Example usage:
if __name__ == "__main__":
    # Initialize an empty linked list
    head = None

    # Insert employees into the sorted linked list
    head = insertEmployee(head, 2, "Aaa", 50000.0)
    head = insertEmployee(head, 1, "Bbb", 60000.0)
    head = insertEmployee(head, 3, "Ccc", 55000.0)

    # Print the sorted linked list
    printLinkedList(head)
