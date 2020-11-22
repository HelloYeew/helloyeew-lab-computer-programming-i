def read_list_while():
    n = 1
    sum = 0
    list = []
    while True:
        num = int(input(f"Enter value{n}: "))
        if num == -99:
            break
        n += 1
        sum = sum+num
        list.append(num)
    return list

def sum_vector(v1,v2):
    i = 0
    listsum = []
    while i < len(v1):
        num = v1[i]+v2[i]
        listsum.append(num)
        i+=1
    return listsum

def diff_vector(v1,v2):
    i = 0
    listsum = []
    while i < len(v1):
        num = v1[i]-v2[i]
        listsum.append(num)
        i+=1
    return listsum

def dot_vector(v1,v2):
    i = 0
    listsum = []
    sum = 0
    while i < len(v1):
        num = v1[i]*v2[i]
        listsum.append(num)
        sum = num + sum
        i+=1
    return sum

print('Enter vector 1:')
v1 = read_list_while()
print('Vector 1:')
print(v1)
print('Enter vector 2:')
n = len(v1)
v2 = read_list_while()
print('Vector 2:')
print(v2)
v_sum = sum_vector(v1, v2)
print('Sum result: ')
print(v_sum)
v_diff = diff_vector(v1, v2)
print('Diff result: ')
print(v_diff)
dot_result = dot_vector(v1, v2)
print('Dot product: ')
print(dot_result)