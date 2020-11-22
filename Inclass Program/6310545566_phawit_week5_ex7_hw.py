def print_every_n(v1,n):
    i = 0
    i += n-1
    print(v1[i])
    while i<len(v1):
        i += n
        if i>=len(v1):
            break
        else:
            print(v1[i])

def print_mod_n(v1,n):
    i = 0
    while i<len(v1):
        if v1[i] % n == 0:
            print(v1[i])
        i += 1

def find_n(v1,n):
    list = []
    i = 0
    while i<len(v1):
        if v1[i] == n:
            list.append(i)
        i+=1
    return list

v1 =[1,2,3,4,5,6,7,8,9,10,11,12,3,3,9,3,99]
n = 3
print('Initial vector:')
print(v1)
print(f'Print every {n}th number:')
print_every_n(v1,n)
print(f'Print numbers divisible by {n}')
print_mod_n(v1,n)
print(f'Print list index of {n}')
index_result = find_n(v1,n)
print(index_result)