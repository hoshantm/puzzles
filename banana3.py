#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:31:56 2024

@author: tarik
"""

import numpy as np

quantity = 2450
capacity = 1000
total_distance = 1000
consumption = 1


distance = 200
round_trips, unmoved_quantity = divmod(quantity, capacity)
trips = round_trips * 2 - 1
remaining_quantity = quantity - trips * distance * consumption
if unmoved_quantity > 2 * distance * consumption:
    unmoved_quantity = 0
    remaining_quantity += unmoved_quantity - 2 * distance * consumption

    



