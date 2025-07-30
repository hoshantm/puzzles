#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:37:26 2020

@author: Tarik Hoshan
"""

from math import ceil

def transport(quantity, distance, capacity, consumption):
    solution = [(0, 0, distance, quantity)]
    qcr = ceil(quantity / capacity)
    moves_left = qcr - 1
    while(distance > 0 and quantity > 0):
        q = quantity - capacity * moves_left
        trips = ceil(quantity / capacity) * 2 - 1
        d = min(q / consumption / trips, distance)
        distance = distance - d
        q = min(q, trips * d * consumption)
        new_quantity = quantity - q
        solution.append((d, q, distance, new_quantity))
        quantity = new_quantity
        moves_left -= 1
        
    return solution

def run_and_print_solution(quantity, distance, capacity, consumption):
    print('   Quantity: %d' % quantity)
    print('   Distance: %d' % distance)
    print('   Capacity: %d' % capacity)
    print('Consumption: %d\n' % consumption)
    solution = transport(quantity, distance, capacity, consumption)
    from tabulate import tabulate
    print(tabulate(solution, ["Distance Travelled", "Quantity Consumed", 'Distance Remaining', 'Quantity Remaining'], tablefmt="grid"))
    if solution[-1][2] > 0:
        print('No solution')
       
"""
Plot maximum net quenity delivered in function of distance
"""
def plot_quantity_delivered_vs_distance(quantity, capacity, consumption):
    distance = 0
    distances = []
    quantities = []
    while True:
        solution = transport(quantity, distance, capacity, consumption)
        if solution[-1][2] > 0:
            break
        else:
            distances.append(distance)
            quantities.append(solution[-1][3])
            
        distance += 1
        
    from matplotlib import pyplot as plt
    plt.plot(distances, quantities)
    plt.title('Quantity delivered in function of distance\nStart quantity = %d, Consumption per unit distance = %d' % (quantity, consumption))
    plt.xlabel('Distance')
    plt.ylabel('Quantity Delivered')
    plt.xlim((0, distances[-1]))
    plt.ylim((0, quantity))
  
"""
Plot maximum range in function of available quantity
"""
def plot_range_vs_quantity(max_quantity, capacity, consumption):
    distances = []
    quantities = []
    
    def transport_remainder(distance, quantity, capacity, consumption):
        solution = transport(quantity, distance, capacity, consumption)
        remaining_distance = solution[-1][2]
        remaining_quantity = solution[-1][3]
        if remaining_distance == 0:
            return remaining_quantity
        else:
            return -remaining_distance * consumption
        
    from scipy.optimize import root_scalar
    
    for quantity in range(max_quantity):
        bracket=(0, quantity / consumption)
        args = (quantity, capacity, consumption)
        solution = root_scalar(transport_remainder, args=args, bracket=bracket)
        distance = solution.root
        quantities.append(quantity)
        distances.append(distance)     
        
    from matplotlib import pyplot as plt
    plt.plot(quantities, distances)
    plt.title('Range vs Quantity\nCapacity = %d, Consumption per unit distance = %d' % (capacity, consumption))
    plt.xlabel('Quantity')
    plt.ylabel('Range')    
    
"""
Plot quantity necessary vs range
"""
def plot_quantity_vs_range(max_distance, capacity, consumption):
    distances = []
    quantities = []
    
    def transport_remainder(quantity, distance, capacity, consumption):
        solution = transport(quantity, distance, capacity, consumption)
        remaining_distance = solution[-1][2]
        remaining_quantity = solution[-1][3]
        if remaining_distance == 0:
            return remaining_quantity
        else:
            return -remaining_distance * consumption
        
    from scipy.optimize import root_scalar
    
    delta_distance = 10
    max_bracket = 1000
    for distance in (i * delta_distance for i in range(int(max_distance/delta_distance))):
        args = (distance, capacity, consumption)
        calculated = False
        while not calculated:
            try:
                bracket=(0, max_bracket)
                solution = root_scalar(transport_remainder, args=args, bracket=bracket)
                calculated = True
            except ValueError:
                max_bracket *= 2
            
        quantity = solution.root
        distances.append(distance)     
        quantities.append(quantity)
        
    from matplotlib import pyplot as plt
    plt.plot(distances, quantities)
    plt.title('Quantity vs Range\nCapacity = %d, Consumption per unit distance = %d' % (capacity, consumption))
    plt.xlabel('Range')    
    plt.ylabel('Quantity')
            
if __name__ == '__main__':
    quantity = 2250
    capacity = 1000
    distance = 1000
    consumption = 1
    run_and_print_solution(quantity, distance, capacity, consumption)        

    