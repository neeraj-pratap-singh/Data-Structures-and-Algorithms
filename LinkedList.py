class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            
            current.next=newnode
    def insertAtStart(self,value):
        newnode=Node(value)
        newnode.next=self.head
        self.head=newnode


    def insertAfterNode(self,value,afterNode):
        newnode=Node(value)
        current=self.head
        while(current.value != afterNode ):
            current=current.next

        newnode.next=current.next
        current.next=newnode

    def display(self):
        current=self.head
        while(current is not None):
            print(current.value,end="->")
            current=current.next
        
if __name__=="__main__":
    obj=LinkedList()
    obj.insertAtStart(20)
    obj.insertAfterNode(50,20)
    obj.insertAtEnd(100)
    obj.insertAtStart(0)
    obj.display()


