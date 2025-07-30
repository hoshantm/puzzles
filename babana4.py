#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:47:11 2024

@author: tarik
"""

import matplotlib.pyplot as plt

def f(capacity, consumption, quantity, distance):
    total_arrived = 0.0
    movable = min(quantity, capacity)
    arrived = movable - distance * consumption
    quantity -= movable
    total_arrived += arrived
    while quantity > 0 and 2 * consumption * distance <= min(quantity, capacity):
        movable = min(quantity, capacity)
        arrived = movable - 2 * distance * consumption
        quantity -= movable
        total_arrived += arrived
        
    return total_arrived


xs = list(range(1001))
ys = [f(1000, 1, 2000, x) * x for x in xs]
plt.plot(xs, ys)


quantity = 2000
for i in range(1):
    quantity = f(1000, 1, quantity, 333)
       