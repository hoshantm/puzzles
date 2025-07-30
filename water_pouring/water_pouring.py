#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:02:36 2018

@author: tarik
"""
from collections import deque

class node:
    def __init__(self, quantities, parent):
        self.quantities = quantities
        self.parent = parent
        
    def __str__(self):
        return 'quantities={}, has_parent={}'.format(self.quantities, self.parent!=None)
    
def visited(node, quantities):
    while True:
        if node.quantities == quantities:
            return True
        elif node.parent == None:
            return False
        else:
            node = node.parent
        
from itertools import groupby
def get_quantity_by_count(quantities):
    return [(g[0], sum(1 for _ in g[1])) for g in groupby(sorted(quantities))]

def gen_solution_found(final_quantities):
    def solution_found(quantities):
        quantities_copy = quantities.copy()
        for quantity in final_quantities:
            if quantity in quantities_copy:
                quantities_copy.remove(quantity)
            else:
                return False
            
        return True
    
    return solution_found

def gen_solution(solution_node):
    solution_quantities_list=[]
    while True:
        solution_quantities_list.append(solution_node.quantities)
        solution_node = solution_node.parent
        if solution_node == None:
            break
        
    solution_quantities_list.reverse()
    return solution_quantities_list    
        
def solver(capacities, initial_quantities, final_quantities, allow_empty=False, allow_fill=False):
    solution_found = gen_solution_found(final_quantities)

    node_queue = deque([node(initial_quantities, None)])
    while True:
        if len(node_queue) == 0:
            return 
            
        current_node = node_queue.popleft()
        current_quantities = current_node.quantities
        for i, q_from in enumerate(current_quantities):
            for j, q_to in enumerate(current_quantities):
                capacity_to = capacities[j]
                if i != j and q_from != 0 and q_to < capacity_to:
                    new_quantities = current_quantities.copy()
                    q_transfer = min(capacity_to - q_to, q_from)
                    new_quantities[i]-=q_transfer
                    new_quantities[j]+=q_transfer
                    if not visited(current_node, new_quantities):
                        new_node = node(new_quantities, current_node)
                                                                       
                        if solution_found(new_quantities):
                            yield gen_solution(new_node)
                        else:
                            node_queue.append(new_node)


            if allow_empty and q_from > 0:
                new_quantities = current_quantities.copy()
                new_quantities[i] = 0
                if not visited(current_node, new_quantities):
                    new_node = node(new_quantities, current_node)
                                                                   
                    if solution_found(new_quantities):
                        yield gen_solution(new_node)
                    else:
                        node_queue.append(new_node)


            if allow_fill and q_from < capacities[i]:
                new_quantities = current_quantities.copy()
                new_quantities[i] = capacities[i]
                if not visited(current_node, new_quantities):
                    new_node = node(new_quantities, current_node)
                                                                   
                    if solution_found(new_quantities):
                        yield gen_solution(new_node)
                    else:
                        node_queue.append(new_node)


def solve(capacities, initial_quantities, final_quantities, allow_empty=False, allow_fill=False):
    solver_iterator = solver(capacities, initial_quantities, final_quantities, allow_empty=allow_empty, allow_fill=allow_fill)
    solution = next(solver_iterator, None)
    return solution

                       
def solve_and_print(capacities, initial_quantities, final_quantities, allow_empty=False, allow_fill=False, n_solutions=1):
    solver_iterator = solver(capacities, initial_quantities, final_quantities, allow_empty=allow_empty, allow_fill=allow_fill)
    i = 0
    while i<n_solutions:
        solution = next(solver_iterator, None)
        if solution != None:
            print('Solution found in {} moves:'.format(len(solution)-1))
            for move, quantities in enumerate(solution):
                print('{} - {}'.format(move, quantities))
            print(' ' * 20)
        else:
            if i==0:
                print('No solution found.')
            elif i+1<n_solutions:
                print('Only {} solutions found'.format(i+1))
            break
        i+=1

def solve_standard_problem(n_solutions=1):
    capacities=[8, 5, 3]
    initial_quantities=[8, 0, 0]
    final_quantities = [4, 4]
    solve_and_print(capacities, initial_quantities, final_quantities, n_solutions=n_solutions)
        

def find_toughest():
    capacities = [13, 7, 5]
    max_total_quantity = sum(capacities)
    max_steps = 0
    for i in range(min(capacities[0], max_total_quantity), -1, -1):
        for j in range(min(capacities[1], max_total_quantity-i), -1, -1):
            for k in range(min(capacities[2], max_total_quantity-i-j), -1, -1):
                initial_quantities = [i, j, k]
                total_quantity = sum(initial_quantities)
                for l in range(min(total_quantity, capacities[0])+1):
                    for m in range(min(total_quantity-l, capacities[1])+1):
                        n = total_quantity - l - m
                        if n > capacities[2]:
                            continue
                        final_quantities = [l, m, n]
                        solution = solve(capacities, initial_quantities, final_quantities)
                        if (solution != None and len(solution) > max_steps):
                            max_steps = len(solution)
                            print(f'{max_steps-1} steps')
                            print(capacities)
                            print(initial_quantities)
                            print(final_quantities)
                            print('-'*20)
                    
if __name__ == '__main__':
    #solve_standard_problem(n_solutions=3)
    find_toughest()
    """
    capacities = [13, 7, 5]
    initial_quantities = [13, 0, 0]
    final_quantities = [12, 0, 1]
    solve_and_print(capacities, initial_quantities, final_quantities, n_solutions=1)
    """
    