#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:06:27 2023

@author: tarik
"""
from math import fmod, floor

def f(quantity, distance, capacity, consumption, remaining_distance):
    rounds = floor(quantity / capacity)
    quantity_moved = rounds * (capacity - 2 * distance * consumption)
    remaining_quantity =  fmod(quantity, capacity)
    if remaining_quantity > 2 * consumption:
        rounds += 1
        quantity_moved += remaining_quantity - distance
    else:
        quantity_moved += distance * consumption
        
    return quantity_moved
        
        