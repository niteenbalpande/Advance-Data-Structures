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
# double_hashing.delete(27)
# print( double_hashing(values, 10, 7) )

