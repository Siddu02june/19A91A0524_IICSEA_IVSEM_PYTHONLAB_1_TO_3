# Exp 1.2) Implement a python script to purposefully raise Indentation Error and Correct it.
num = int(input('Enter a number: '))
i = 1
while i<=num:
print(i)		#Raises Indentation error
	i += 1

'''
Output:
  File "Exp 1.2 Indentation Error.py", line 6
    print(i)            #Raises Indentation error
    ^
IndentationError: expected an indented block
'''

num = int(input('Enter a number: '))
i = 1
while i<=num:
	print(i)	#Correction of this Indentation Error
	i += 1

'''
Output:
Enter a number: 8
1
2
3
4
5
6
7
8
'''
