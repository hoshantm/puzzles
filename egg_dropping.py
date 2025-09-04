#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 17:32:00 2018

@author: Tarik Hoshan
"""

from functools import lru_cache
from operator import itemgetter

# Change the call to func(n_eggs, l_floor, h_floor) to func(n_eggs, 1, h_floor - l_floor + 1)
# with the assumption that the result is equivalent.
def shift_params(func):
    def shift_params_func(n_eggs, l_floor, h_floor):
        cost, floor = func(n_eggs, 1, h_floor - l_floor + 1)
        floor += l_floor - 1
        return cost, floor
    return shift_params_func

@shift_params
@lru_cache(maxsize=100000)
def min_test_floor(n_eggs, l_floor, h_floor):
    assert n_eggs >= 1
    assert h_floor >= l_floor
    assert l_floor == 1
    
    if n_eggs == 1 or 0 <= h_floor - l_floor <= 1:
        return h_floor - l_floor + 1, l_floor
    else:
        all_max = (max(min_test_floor(n_eggs, test_floor+1, h_floor) if test_floor < h_floor else (-1, None), \
                       min_test_floor(n_eggs-1, l_floor, test_floor-1) if test_floor > l_floor else (-1, None), \
                       key=itemgetter(0)) \
                   for test_floor in range(l_floor, h_floor+1))

        index, minimum=min(enumerate(all_max), key=lambda m: m[1][0])
        try_floor = index + l_floor
        min_tests = minimum[0] + 1
        return min_tests, try_floor
    
def machine_solve(n_eggs, n_floors):      
    r_eggs = n_eggs
    l_floor = 1
    h_floor = n_floors
    trial = 1
    while True:
        _, selected_floor = min_test_floor(r_eggs, l_floor, h_floor)
        answer = input(f'Trial number {trial}, release egg from floor {selected_floor}. Did the egg break? y/n: ')
        if answer == 'y':
            h_floor = selected_floor - 1
            r_eggs -= 1
            print(f'\n{r_eggs} remaining eggs.')
            if l_floor > h_floor:
                highest_safe_floor = l_floor - 1
                if highest_safe_floor >= 1:
                    print(f'\nMaximum floor that does not break eggs is {highest_safe_floor}.\n')
                else:
                    print("\nNo floor is safe to drop eggs.\n")
                break
        else:
            l_floor = selected_floor + 1
            if l_floor > h_floor:
                print(f'\nMaximum floor that does not break eggs is {h_floor}.\n')
                break
            
        print(f'\nTesting floors between {l_floor} and {h_floor}')
        trial+=1
        
    print(f'Floor found in {trial} trials.')
    print(f'Broke {n_eggs - r_eggs} eggs in the process.')

if __name__ == "__main__":
    
    while True:
        try:
            str_floors=input('Number of floors: ')
            n_floors = int(str_floors)
        except ValueError:
            print('Invalid number of floors')
            
        if n_floors < 2:
            print('You should have at least two floors\n')
        else:
            break
        
    while True:
        try:
            str_eggs=input('Number of eggs: ')
            n_eggs = int(str_eggs)
        except ValueError:
            print('Invalid number of eggs')
            
        if n_floors < 1:
            print('You should have at least one egg\n')
        else:
            break
        
    machine_solve(n_eggs, n_floors)
    
