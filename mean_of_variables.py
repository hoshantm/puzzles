#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:19:33 2024

@author: tarik
"""

import cvxpy as cp

N = 3
x = cp.Variable(N)
z = cp.Variable(N)

sum_of_positive_x = cp.sum([cp.max(xi, 0) for xi in x]) 


z * x >= 0
z in {0, 1}

count_of_positive_x = cp.sum(z)
mean_of_positive_x = sum_of_positive_x / count_of_positive_x
constraints = [x[0] <= 10, x[1] <= -5, x >= -20, mean_of_positive_x == 5, x[2] >= 2]

prob = cp.Problem(cp.sum(x), constraints)
prob.solve()
