#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:04:13 2018

@author: tarik

Euler project problem 502
https://projecteuler.net/problem=502

Broken version
"""

def castles(w, h, must_reach, even):
    assert w>0, 'Width must be positive'
    assert h>0, 'Height must be positive'

    if h==1 and must_reach:
        if even:
            return 0
        else:
            return 1
    elif h==1 and not must_reach:
        if even:
            return 1
        else:
            return 0
    elif w==1 and must_reach:
        if even:
            if h % 2 == 0:
                return 1
            else:
                return 0
        else:
            if h % 2 == 1:
                return 1
            else:
                return 0
    elif w==1 and not must_reach:
        if even:
            return (h-1) // 2
        else:
            return (h-1) // 2 + 1

    else:
        total = 0
        for leading_empty in range(w-2):
            for left_width in range(1, w-leading_empty-1):
                if even:
                    total+=castles(left_width, h-1, True, True) * castles(w-leading_empty-left_width-1, h, False, True)
                    total+=castles(left_width, h-1, False, True) * castles(w-leading_empty-left_width-1, h, True, True)
                    total+=castles(left_width, h-1, True, True) * castles(w-leading_empty-left_width-1, h, True, True)
                    total+=castles(left_width, h-1, True, False) * castles(w-leading_empty-left_width-1, h, False, False)
                    total+=castles(left_width, h-1, False, False) * castles(w-leading_empty-left_width-1, h, True, False)
                    total+=castles(left_width, h-1, True, False) * castles(w-leading_empty-left_width-1, h, True, False)
                else:
                    total+=castles(left_width, h-1, True, True) * castles(w-leading_empty-left_width-1, h, False, False)
                    total+=castles(left_width, h-1, False, True) * castles(w-leading_empty-left_width-1, h, True, False)
                    total+=castles(left_width, h-1, True, True) * castles(w-leading_empty-left_width-1, h, True, False)
                    total+=castles(left_width, h-1, True, False) * castles(w-leading_empty-left_width-1, h, False, True)
                    total+=castles(left_width, h-1, False, False) * castles(w-leading_empty-left_width-1, h, True, True)
                    total+=castles(left_width, h-1, True, False) * castles(w-leading_empty-left_width-1, h, True, True)
                    
        if not must_reach and even:
            total+=1
            
        return total
        
        
        #return sum(castles(left_width, h-1) * castles(w-leading_empty-left_width-1,h) + 1 for leading_empty in range(w+1) for left_width in range(1, w+1-leading_empty))
    
if __name__ == "__main__":
    """
    w=1
    h=2
    l = list(((left_width, h-1, w-leading_empty-left_width-1,h) for leading_empty in range(w+1) for left_width in range(1, w+1-leading_empty)))
    print(l)
    
    w=2
    h=2
    l = list(((left_width, h-1, w-leading_empty-left_width-1,h) for leading_empty in range(w+1) for left_width in range(1, w+1-leading_empty)))
    print(l)
    """
    from datetime import datetime
    t1 = datetime.now()
    print(castles(1,2, True, True))
    print(castles(2,2, True, True))
    print(castles(3,2, True, True))
    print(castles(4,2, True, True))
    t2 = datetime.now()
    print(t2 - t1)