from listoperations import *

n = int(input('Enter number of Elements: '))
lst = []
for i in range(n):
    lst.append(int(input()))

print(list_sum(lst))
print(list_sort(lst))

s = input()

print(string_list_conversion(s))

'''
Output:
Enter number of Elements: 7
8
9
4
2
3
5
1
32
[1, 2, 3, 4, 5, 8, 9]
PyModules
['P', 'y', 'M', 'o', 'd', 'u', 'l', 'e', 's']
'''
