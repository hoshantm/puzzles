#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:29:00 2020

Find solutions to 

@author: Tarik Mohamed Hoshan
"""

from itertools import groupby

def get_state(state, move):
    possible_positions = (i for i in state if i != move)
        
    new_state = set()
    for i in possible_positions:
        if i == 0:
            new_state.add(1)
        elif i == N - 1:
            new_state.add(N - 2)
        else:
            new_state.add(i-1)
            new_state.add(i+1)
            
    return new_state
        
def find_solutions_recursively(solutions, state, move, visited, moves, n, max_solutions):
    if max_solutions != None and len(solutions) >= max_solutions:
        return
    
    for i in range(n):
        new_state = get_state(state, i)
        if new_state in visited:
            pass
        else:
            visited.append(new_state)
            moves.append(i)
            if new_state == set():
                solutions.append((visited.copy(), moves.copy()))
            else:
                find_solutions_recursively(solutions, new_state, i, visited, moves, n, max_solutions)            
            visited.pop()
            moves.pop()
            
def find_solutions(n, max_solutions):
    solutions = []
    start_state = {i for i in range(n)}
    visited = [start_state]
    moves = [None]
    find_solutions_recursively(solutions, start_state, None, visited, moves, n, max_solutions)
    return solutions
                    
def print_solution(solution):
    for state, move in zip(solution[0], solution[1]):
        if move != None and state != set():
            print(move)
        if state != set():
            print(state)
            
def find_and_print_solutions(n):
    MAX_SOLUTIONS = None
    PRINT_SOLUTIONS = True
    
    solutions = find_solutions(n, MAX_SOLUTIONS)   
    solutions = sorted(solutions, key=lambda solution: len(solution[0]))    
    print('%d solutions found:' % len(solutions))    
    solution_groups = ((g[0], list(g[1])) for g in groupby(solutions, lambda solution: len(solution[0])))
    
    for solution_length, solution_group in solution_groups:
        print('- %d solutions of length %d' % (len(solution_group), solution_length))
        if PRINT_SOLUTIONS:
            for solution in solution_group:
                print_solution(solution)
                print('======================================')
                
    print('\nNote: Only unique solutions with no cycle are considered.')
    
                  
if __name__ == '__main__':
    N = 5 # Number of boxes where the cat can hide
    
    find_and_print_solutions(N)

