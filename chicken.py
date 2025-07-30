#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:21:42 2020

@author: tarik
"""

import numpy as np

n = 10000
draws = 10000

total = 0
for i in range(draws):
    chickens = np.random.choice(a=[False, True], size=n)
    chickens = chickens > 0
    chickens = np.logical_and(np.roll(chickens, shift=1), np.logical_not(np.roll(chickens, shift=-1)))
    unpecked = np.sum(chickens)
    total += unpecked
    
print(total / draws)

