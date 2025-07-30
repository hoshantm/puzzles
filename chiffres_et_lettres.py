def copy_and_remove(l, i, j):
    if i > j:
        i, j = j, i
    l = l.copy()
    l.pop(j)
    l.pop(i)
    return l

def solve(numbers, target, trace=[]):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            
            if i == j:
                continue
            
            n = numbers[i]
            m = numbers[j]

            trace.append(f'{n} + {m} = {n+m}')
            if n + m == target:
                return True
            else:
                new_numbers = copy_and_remove(numbers, i, j)
                new_numbers.append(n+m)

                if solve(new_numbers, target, trace):
                    return True

            trace.pop()

            trace.append(f'{n} - {m} = {n-m}')
            if n - m == target:
                return True
            else:
                new_numbers = copy_and_remove(numbers, i, j)
                new_numbers.append(n+m)

                if n > m and solve(new_numbers, target, trace):
                    return True

            trace.pop()

            trace.append(f'{n} x {m} = {n*m}')
            if n * m == target:
                return True
            else:
                new_numbers = copy_and_remove(numbers, i, j)
                new_numbers.append(n*m)
                
                if solve(new_numbers, target, trace):
                    return True
 
            trace.pop()

            trace.append(f'{n} / {m} = {n//m}')

            if n / m == n // m == target and m != 0:
                return True
            elif n / m == n // m and m != 0:
                new_numbers = copy_and_remove(numbers, i, j)
                new_numbers.append(n//m)

                if solve(new_numbers, target, trace):
                    return True 

            trace.pop()

    return False

 

numbers = [8, 4, 4, 6, 8, 9]

target = 594

trace=[]

solve(numbers, target, trace)

print(trace)