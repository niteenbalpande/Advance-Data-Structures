#singly LL
class Node:# Create a node
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None 
    def insertAtBeginning(self, data):# Insert at the beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, data):# Insert after a node
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, data):
		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
        new_node = Node(data)

		# 4. If the Linked List is empty, then make the
		# new node as head
        if self.head is None:
            self.head = new_node
            return

		# 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

		# 6. Change the next of last node
        last.next = new_node
    # Deleting a node
    def deleteNode(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next


    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next
if __name__ == '__main__':

    SLList = LinkedList()
    SLList.append(7)
    SLList.insertAtBeginning(2)
    SLList.insertAtBeginning(3)
    SLList.insertAfter(SLList.head.next, 5)
    print('Singly linked list:')
    SLList.printList()

    print("\nAfter deleting an element:")
    SLList.deleteNode(2)
    SLList.printList()