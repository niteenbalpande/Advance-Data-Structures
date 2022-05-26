#Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.head = None
    # Insert Element to Empty list
    def insertAtBeginning(self, data):
            new_node = Node(data)
            self.head = new_node

    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Delete the elements from the start
    def deleteNode(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None;
    # Delete the elements from the end
    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")
# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.insertAtBeginning(10)
# Insert the element at the end
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)
# Display Data
NewDoublyLinkedList.Display()
# Delete elements from start
NewDoublyLinkedList.deleteNode()
NewDoublyLinkedList.deleteNode()
# Display Data
NewDoublyLinkedList.Display()