# -*- coding: utf-8 -*-
"""
Created by 203 Inc.
@author: 
Name -Niteen Balpande
Enroll No- VP21CSEN0100001
Specialization- CSE
""" 
def badCharHeuristic(string, size):
    NO_OF_CHARS = 256
    badChar = [-1]*NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i;
    return badChar
def search(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while(s <= n-m):
        j = m-1
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])
def main():
    txt = "XIOGITATSDFMAGGITAMATCHGIJYTAM"
    pat = "GITAM"
    search(txt, pat)
if __name__ == '__main__':
    main()
