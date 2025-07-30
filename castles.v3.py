#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:04:13 2018

@author: tarik

Euler project problem 502
https://projecteuler.net/problem=502

Works correctly but too slow to solve the problem as stated:
    Find (F(1012,100) + F(10000,10000) + F(100,1012)) mod 1 000 000 007
"""
from functools import lru_cache
import sys

@lru_cache(100000000)
def castles_max_height(w, h, base, even):
    #assert h>0, 'Height should be greater than zero'
    #assert w>=-1, 'Width should be greater or equal to -1'
    if w<=0:
        if even:
            return 1
        else:
            return 0
    elif h == 1:
        if even and not base or not even and base:
            return 1
        else:
            return 0
    else:
        total = 0
        for leading_empty in range(w):
            for left_width in range(1, w+1-leading_empty):
                total+=castles_max_height(left_width, h-1, True, base and not even or not base and even) * castles_max_height(w-leading_empty-left_width-1,h,False,True)
                total+=castles_max_height(left_width, h-1, True, base and even or not base and not even) * castles_max_height(w-leading_empty-left_width-1,h,False,False)
                
        if base and not even or not base and even:
            total+=1
            
        return total

def castles(w, h):
    count1 = castles_max_height(w, h, True, True)
    count2 = castles_max_height(w, h-1, True, True)
    count = count1 - count2
    return count
           
if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    print(4,2)
    assert castles(4,2) == 10
    print(13,10)
    assert castles(13,10) == 3729050610636
    print (10, 13)
    assert castles(10,13) == 37959702514
    assert castles(100,100) % 1000000007 == 841913936
    print('Verification done')
    print('Cache hit info: {}', castles_max_height.cache_info())

            