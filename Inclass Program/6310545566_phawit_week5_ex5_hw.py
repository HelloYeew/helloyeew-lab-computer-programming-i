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

print("Enter vector 1:")
llist1 = read_list_while()
print("Vector 1:")
print(llist1)
print("Enter vector 2:")
llist2 = read_list_while()
print("Vector 2:")
print(llist1)