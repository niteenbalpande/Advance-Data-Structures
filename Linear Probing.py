# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:30:58 2021

@author:mr. Niteen Balpande @2o3 Products and Services.
"""
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


