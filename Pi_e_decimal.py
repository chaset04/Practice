# Program that takes user input to select Pi or e, then asks user how many
# decimal places they would like to print out and prints result


import math


def print_e(num):
	e = math.e
	print(f"e to the {num} decimal place is {e:.{num}f}")


def print_pi(num):
	pi = math.pi
	print(f"Pi to the {num} decimal place is {pi:.{num}f}")


def main():
	choice = int(input('*** Pi and e decimal program ***\n1. e to the nth place.\n2. Pi to the nth place.\nChoice: '))
	while choice != 3:
		if choice == 1:
			print_e(int(input('To what decimal place do you want to see e? ')))
		if choice == 2:
			print_pi(int(input('To what decimal place do you want to see pi? ')))
		if choice > 3:
			print('Invalid choice\n')
		choice = int(input('\nMake another selection, or enter 3 to quit: '))
	print('\nExiting program...')


main()
