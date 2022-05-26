#!/usr/bin/env python
# coding: utf-8

# In[7]:


#singly LL
class Node:# Create a node
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None 
    def insertAtBeginning(self, new_data):# Insert at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):# Insert after a node
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, new_data):
		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
        new_node = Node(new_data)

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

    llist = LinkedList()
    llist.append(7)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAfter(llist.head.next, 5)
    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(4)
    llist.printList()


# In[22]:


#Circuler LL
class Node:
	def __init__(self, next = None, data = None):
		self.next = next
		self.data = data

# Function to insert a node at the beginning of
# a Circular linked list
def push(head_ref, data):

	# Create a new node and make head as next
	# of it.
	ptr1 = Node()
	ptr1.data = data
	ptr1.next = head_ref

	# If linked list is not None then set the
	# next of last node
	if (head_ref != None) :
		
		# Find the node before head and update
		# next of it.
		temp = head_ref
		while (temp.next != head_ref):
			temp = temp.next
		temp.next = ptr1
	
	else:
		ptr1.next = ptr1 # For the first node

	head_ref = ptr1
	return head_ref

# Function to print nodes in a given
# circular linked list
def printList( head):

	temp = head
	if (head != None) :
		while(True) :
			print( temp.data, end = " ")
			temp = temp.next
			if (temp == head):
				break
	print()

# Function to delete a given node from the list
def deleteNode( head, key) :

	# If linked list is empty
	if (head == None):
		return
		
	# If the list contains only a single node
	if((head).data == key and (head).next == head):
	
		head = None
	
	last = head
	d = None
	
	# If head is to be deleted
	if((head).data == key) :
		
		# Find the last node of the list
		while(last.next != head):
			last = last.next
			
		# Point last node to the next of head i.e.
		# the second node of the list
		last.next = (head).next
		head = last.next
	
	# Either the node to be deleted is not found
	# or the end of list is not reached
	while(last.next != head and last.next.data != key) :
		last = last.next

	# If node to be deleted was found
	if(last.next.data == key) :
		d = last.next
		last.next = d.next
	
	else:
		print("no such keyfound")
	
	return head

head = None
head = push(head, 2)
head = push(head, 5)
head = push(head, 7)
head = push(head, 8)
head = push(head, 10)

print("List Before Deletion: ")
printList(head)

head = deleteNode(head, 7)

print( "List After Deletion: ")
printList(head)


# In[23]:


#Doubly LL
# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")
    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None;
    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")
# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.InsertToEmptyList(10)
# Insert the element at the end
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)
# Display Data
NewDoublyLinkedList.Display()
# Delete elements from start
NewDoublyLinkedList.DeleteAtStart()
# Delete elements from end
NewDoublyLinkedList.DeleteAtStart()
# Display Data
NewDoublyLinkedList.Display()


# In[8]:


#Dictionary using hashing
# Function to display hashtable
def display_hash(hashTable):
	
	for i in range(len(hashTable)):
		print(i, end = " ")
		
		for j in hashTable[i]:
			print("-->", end = " ")
			print(j, end = " ")
			
		print()

# Creating Hashtable as
# a nested list.
HashTable = [[] for _ in range(10)]

# Hashing Function to return
# key for every value.
def Hashing(keyvalue):
	return keyvalue % len(HashTable)


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
	
	hash_key = Hashing(keyvalue)
	Hashtable[hash_key].append(value)

# Driver Code
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 20, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 21, 'Punjab')
insert(HashTable, 21, 'Noida')

display_hash (HashTable)


# In[25]:


import numpy as np
class Hash_table() :
    
    def __init__(self,size) :
        self.size = size
        self.hashtable = np.array([None]*self.size)
        
    def hash(self,key) :
        index = key%10 
        
        if self.hashtable[index] == None :
            return index
        else :
            
            # Implementing linear probing
            while self.hashtable[index] != None :
                index = (index+1)%10
                
            return index
        
    def insert(self,key) :
        
        index = self.hash(key)
        self.hashtable[index] = key    
    
    def delete(self,key):
        self.size-=1
        index=self.hash(key)
        while index is None:
            self.size+=1
            break
        self.hashtable[index] = None
        
    def print_hashtable(self) :
        
        print("Hash table is :-\n\nindex \t value")
        for x in range(len(self.hashtable)) :
            print(x,"\t",self.hashtable[x])

HT = Hash_table(10) #sizzzz
HT.insert(20)
HT.insert(7)
HT.insert(9)
HT.insert(13)
HT.insert(2)
HT.insert(14)
HT.insert(12)
HT.insert(15)

HT.print_hashtable()
HT.delete(0)   

HT.print_hashtable()


# In[30]:


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:51:08 2021

@author:mr. Niteen Balpande @2o3 Products and Services.
"""
def double_hashing(keys, hashtable_size, double_hash_value):
    hashtable_list = [None] * hashtable_size
    for i in range(len(keys)):
        hashkey = keys[i] % hashtable_size
        if hashtable_list[hashkey] is None:
            hashtable_list[hashkey] = keys[i]
        else:
            new_hashkey = hashkey
            while hashtable_list[new_hashkey] is not None:
                steps = double_hash_value - (keys[i] % double_hash_value)
                new_hashkey = (new_hashkey + steps) % hashtable_size  ## problem 1 is here
            hashtable_list[new_hashkey] = keys[i]
    return hashtable_list  ## problem 2 is here

    def delete(self, key):
        index = self.search(key)
        if index > -1:
            self.state[index] = -1
values = [3, 22, 27, 40, 42, 11, 19]
print( double_hashing(values, 10, 7) )
#hashtable_list.delete()
#print( double_hashing(values, 10, 7) )


# In[16]:


# Quick Sort
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
  return i + 1

def qs(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    qs(arr, low, pi - 1)
    qs(arr, pi + 1, high)
    
data = [8, 7, 2, 41, 0, 9, 6]
size = len(data)
qs(data, 0, size - 1)
print(' Quick Sorted list')
print(data)


# In[17]:


# MergeSort
def mergeSort(array):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        # Sort the two halves
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Merge Sorted array is: ")
    printList(array)


# In[18]:


#heep sort
def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
def heapSort(arr):
      n = len(arr)
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
          heapify(arr, i, 0)
  
  
arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Heap Sorted array is")
for i in range(n):
      print("%d " % arr[i], end='')


# In[19]:


#selection sort
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)


# In[ ]:




