#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 17:32:00 2018

@author: Tarik Hoshan
"""

from functools import lru_cache
from operator import itemgetter

def shift_params(func):
    def swap_func(n_eggs, l_floor, h_floor=None):
        if h_floor == None:
            l_floor, h_floor = 1, l_floor
            return func(n_eggs, l_floor, h_floor)
        else:
            cost, floor = func(n_eggs, 1, h_floor - l_floor + 1)
            floor += l_floor -1
            return cost, floor
    return swap_func

@shift_params
@lru_cache(maxsize=100000)
def min_test_floor(n_eggs, l_floor, h_floor=None):
    assert n_eggs >= 1
    assert h_floor >= l_floor
    
    if n_eggs == 1 or 0 <= h_floor - l_floor <= 1:
        return h_floor - l_floor + 1, l_floor
    else:
        all_max = (max(min_test_floor(n_eggs, test_floor+1, h_floor) if test_floor < h_floor else (-1, -1), min_test_floor(n_eggs-1, l_floor, test_floor-1) if test_floor > l_floor else (-1, -1)) for test_floor in range(l_floor, h_floor+1))

        index, minimum=min(enumerate(all_max), key=itemgetter(1))
        try_floor = index + l_floor
        min_tests = minimum[0] + 1
        return min_tests, try_floor
    
def machine_solve():
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
        
    r_eggs = n_eggs
    l_floor = 1
    h_floor = n_floors
    trial = 1
    while True:
        _, selected_floor = min_test_floor(r_eggs, l_floor, h_floor)
        answer = input('Trial number {}, release egg from floor {}. Did the egg break? y/n: '.format(trial, selected_floor))
        if answer == 'y':
            h_floor = selected_floor - 1
            if l_floor > h_floor:
                highest_safe_floor = l_floor - 1
                if highest_safe_floor >= 1:
                    print('\nMaximum floor that does not break egg is {0}.\n'.format(highest_safe_floor))
                else:
                    print("\nNo floor is safe to drop eggs.\n")
                break
            else:
                r_eggs -= 1
            print('\n{} remaining eggs.'.format(r_eggs))
        else:
            l_floor = selected_floor + 1
            if l_floor > h_floor:
                print('\nMaximum floor that does not break egg is {0}.\n'.format(h_floor))
                break
            
        print('\nTesting floors between {} and {}'.format(l_floor, h_floor))
        trial+=1

if __name__ == "__main__":
    machine_solve()
    
