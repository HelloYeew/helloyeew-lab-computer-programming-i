def read_one_int(word):
    num = int(input(word))
    return num

def read_two_ints():
    a = int(input("Enter num:"))
    b = int(input("Enter num2:"))
    return a,b
#
# num = read_one_int('Enter num:')
# num2 = read_one_int('Enter num2:')
# print(num+num2)

num,num2 = read_two_ints()
print(num)
print(num2)