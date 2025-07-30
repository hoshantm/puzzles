import numpy as np

DEBUG = False
MAX_ATTEMPTS = 50
PRISONERS = 100
 
def tryit():
    a = np.arange(PRISONERS)
    np.random.shuffle(a)
    for i in range(PRISONERS):
        if DEBUG:
            print(f'prisoner {i}')
        count = 0
        check = i
        while count <= MAX_ATTEMPTS:
            count += 1
            if a[check] == i:
                if DEBUG:
                    print(f'Attempt {count}: Checking box {check} and found my number')
                break
            else:
                if DEBUG:
                    print(f'Attempt {count}: Checking box {check} and found {a[check]}')           
                check = a[check]
           
        if count > MAX_ATTEMPTS:
            if DEBUG:
                print(f'Prisoner {i} failed to find his number in {MAX_ATTEMPTS} attempts')
            return False
       
    return True
 
tries = 100000
success = 0
for i in range(tries):
    if tryit():
        success += 1
       
print(f'Ratio of success = {success / tries}')