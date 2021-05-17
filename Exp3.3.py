'''
3.3)
Implement a python script that prompts the user for a number, and prints that number in words. Example: Input :453 Output :Four Five Three
Input :1000 Output :One Zero ZeroZero
'''

num = input('Enter number: ')

for ch in num:
	if ch == '0':
		print('ZERO',end=' ')
	elif ch == '1':
		print('ONE',end=' ')
	elif ch == '2':
		print('TWO',end=' ')
	elif ch == '3':
		print('THREE',end=' ')
	elif ch == '4':
		print('FOUR',end=' ')
	elif ch == '5':
		print('FIVE',end=' ')
	elif ch == '6':
		print('SIX',end=' ')
	elif ch == '7':
		print('SEVEN',end=' ')
	elif ch == '8':
		print('EIGHT',end=' ')
	elif ch == '9':
		print('NINE',end=' ')
	
'''
Output:

Enter number: 524
FIVE TWO FOUR

Enter number: 0123456789
ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE
'''
