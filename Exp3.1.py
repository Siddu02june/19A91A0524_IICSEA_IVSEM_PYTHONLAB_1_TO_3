'''
3.1)
Implement a python script for checking whether the citizen is eligible for vote or not.
'''

age = int(input('Enter age: '))

if age >= 18:
	print('You are eligible to vote')
else:
	print('You are not eligible to vote')

'''
Output:
Sample Test1
Enter age: 24
You are eligible to vote
Sample Test2
Enter age: 12
You are not eligible to vote
'''
