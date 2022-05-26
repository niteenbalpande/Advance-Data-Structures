# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:48:28 2021

@author:mr. Niteen Balpande @2o3 Products and Services.
"""
hash_table = [[] for _ in range(10)]
print (hash_table)  ##Creating empty hash

def insert(hash_table, key, value):
	hash_key = hash(key) % len(hash_table)
	key_exists = False
	bucket = hash_table[hash_key]	
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			key_exists = True 
			break
	if key_exists:
		bucket[i] = ((key, value))
	else:
		bucket.append((key,value))
insert(hash_table, 10, 'Niteen')
insert(hash_table, 25, 'S')
insert(hash_table, 22, 'Balpande')
insert(hash_table, 23, 'Block')
insert(hash_table, 26, 'Hyperladger')
print (hash_table)