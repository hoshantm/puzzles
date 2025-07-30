#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 18:18:13 2020

@author: tarik
"""

N_BOXES = 5

def find_cat(cat_position, depth, depth_limit):
    if depth > depth_limit:
        return False, None
    
    depth += 1
    
    for check_box in range(N_BOXES):
        if not hide_cat(cat_position, check_box, depth, depth_limit):
            return True, check_box
        
    return False, None
    
    
def hide_cat(cat_position, check_box, depth, depth_limit):
    if cat_position == None:
        valid_moves = [i for i in range(N_BOXES)]
    elif cat_position == 0:
        valid_moves = [1]
    elif cat_position == N_BOXES - 1:
        valid_moves = [N_BOXES - 2]
    else:
        valid_moves = [cat_position - 1, cat_position + 1]
        
    valid_moves = [i for i in valid_moves if i != check_box]
    
    if valid_moves == []:
        return False
        
    for new_cat_position in valid_moves:
        cat_found, _ = find_cat(new_cat_position, depth, depth_limit)
        if not cat_found:
            return True
        
    return False

if __name__ == '__main__':
    depth_limit = 1
    result = hide_cat(2, 2, 0, depth_limit)
    print(result)
        