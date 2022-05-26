# -*- coding: utf-8 -*-
"""
Created by 203 Inc.

@author: Niteens
"""
def BF(s1,s2):
    """ BF algorithm """
    i = 0
    j = 0
    while(i < len(s1) and j < len(s2)):
        if(s1[i] ==  s2[j]):
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if(j >= len(s2)):
        return i - len(s2)
    else:
        return 0

if __name__ == "__main__":
    a1="abcaaaabbbbcccabcbabdbcababababsbbbbnnn"
    a2='ccabcba'
    b=BF(a1,a2)
    print(b)
 #   s0 = "abababab
    s1 = "ababcabcacbab"
    s2 = "abcac"
    print(BF(s1,s2))
