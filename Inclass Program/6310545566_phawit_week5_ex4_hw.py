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

llist1 = read_list_while()
print(llist1)
print(f'{sum(llist1)/len(llist1):.2f}')