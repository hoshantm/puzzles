#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:04:13 2018

@author: tarik

Euler project problem 502
https://projecteuler.net/problem=502

This version calculates total number of castles but does not ensure the height is exactly h. It also
does not meet the even number of blocks criteria.
"""

def castles(w, h):
    if h == 1 or w<=0:
        return 1
    else:
        total = 0
        for leading_empty in range(w):
            for left_width in range(1, w+1-leading_empty):
                total+=castles(left_width, h-1) * castles(w-leading_empty-left_width-1,h)
        total+=1
        return total
        
        
        #return sum(castles(left_width, h-1) * castles(w-leading_empty-left_width-1,h) + 1 for leading_empty in range(w+1) for left_width in range(1, w+1-leading_empty))
    
if __name__ == "__main__":
    w=1
    h=2
    l = list(((left_width, h-1, w-leading_empty-left_width-1,h) for leading_empty in range(w+1) for left_width in range(1, w+1-leading_empty)))
    print(l)
    
    w=2
    h=2
    l = list(((left_width, h-1, w-leading_empty-left_width-1,h) for leading_empty in range(w+1) for left_width in range(1, w+1-leading_empty)))
    print(l)
    
    
    print(castles(1,2))
    print(castles(2,2))
    print(castles(3,2))
    print(castles(4,2))