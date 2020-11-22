def print_list(list):
    for x in list:
        print(x)


def read_list(n):
    i = 1
    listoutput = []
    while i < n + 1:
        value = float(input(f"Enter value{i}: "))
        listoutput.append(value)
        i += 1
    return listoutput


def compute_area_list(list1, list2):
    area_list = []
    n = len(list1)
    for i in range(n):
        area = list1[i] * list2[i]
        area_list.append(area)
    return area_list


n = int(input("Enter n: "))
print("Side 1:")
list1 = read_list(n)
print("Side 2:")
list2 = read_list(n)
a_list = compute_area_list(list1, list2)
print_list(a_list)
