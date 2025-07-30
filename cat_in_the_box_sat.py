from z3 import Solver, Int, AtMost, And, Or, sat
    
if __name__ == "__main__":
    n = 5
    depth = 6
    n_solutions = None # Maximum number of solutions to find or None for all
    print_solutions = True # To print the solutions
    
    s = Solver()
    
    # Create variables
    b = [Int("b_%d" % i) for i in range(depth) ]
    for i in range(depth):
        s.add(b[i] >= 0)
        s.add(b[i] < n)
            
    w = []
    a = []
    a.append(b[0] != 1)
    for j in range(1, n-1):
        a.append(Or(b[0] != j-1, b[0] != j+1))
    a.append(b[0] != n-2)
    w.append(AtMost(*a, 0))
    
    for i in range(1, depth):
        temp = []
        temp.append(And(b[i] != 1, a[1]))
        for j in range(1, n-1):
            temp.append(Or(And(b[i] != j-1, a[j-1]), And(b[i] != j+1, a[j+1])))
        temp.append(And(b[i] != n-2, a[n-2]))
        a = temp
        w.append(AtMost(*a, 0))
        
    exp = Or(w)
    s.add(exp)
    
    solution_count = 0
    while (n_solutions == None or solution_count < n_solutions) and s.check() == sat:
        solution_count = solution_count + 1
        m = s.model()
        if print_solutions:
            for move in sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0])):
                print(move[1])
            print("======================")
                
        s.add(Or([bi != m[bi] for bi in b]))
                                
    if solution_count > 0:
        print('Found %d solutions of length %d' % (solution_count, depth))
    else:
        print('No solution found')
    