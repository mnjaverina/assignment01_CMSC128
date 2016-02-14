#Author: Javerina, Mark Neil G.
#Student Number: 2013-09005
#Lab Section: AB-6L
#A program that translates an input number to words and vice versa.
#Date submitted: February 14, 2016 (hart hart)

#!usr/bin/python

def printMenu():
	print "=====Number Library====="
	print "[1] Digits to Words"
	print "[2] Words to Digits"
	print "[3] Currency to Words"
	print "[4] Words to Currency"
	print "[5] Exit"
	print "======================"
	choice = input("Choice:")
	return choice

def wordstoNum():
	digit = raw_input("Enter a 7-digit max number (in words):")
	number = digit.split(" ")
	word = ' '
	for i in range(0, len(digit)+1):                                                                          
		
		if number[i] == 'one':
			word = word + '1'
		elif number[i] == 'two':
			word = word + '2'
		elif number[i] == 'three':
			word = word + '3'
		elif number[i] == 'four':
			word = word + '4'
		elif number[i] == 'five':
			word = word + '5'
		elif number[i] == 'six':
			word = word + '6'
		elif number[i] == 'seven':
			word = word + '7'	
		elif number[i] == 'eight':
			word = word + '8'
		elif number[i] == 'nine':
			word = word + '9'
		elif number[i] == 'ten':
			word = word +'10'
		elif number[i] == 'twenty':
			word = word +'20'
		elif number[i] == 'thirty':
			word = word +'30'
		elif number[i] == 'forty':
			word = word +'40'
		elif number[i] == 'fifty':
			word = word +'50'
		elif number[i] == 'sixty':
			word = word +'60'
		elif number[i] == 'eighty':
			word = word +'80'
		elif number[i] == 'ninety':
			word = word +'90'
		else:
			continue	


	return word

def numtoWords():
	digit = raw_input("Enter a 7-digit max number(in symbols):")
	while digit:
		digit, number = divmod(int(digit), 10)
		word = " "
	#for number in digit:
		if number == 1:
			word = word + 'one '
		elif number == 2:
			word = word + 'two '
		elif number == 3:
			word = word + 'three'
		elif number == 4:
			word = word + 'four '
		elif number == 5:
			word = word + 'five'
		elif number == 6:
			word = word + 'six '
		elif number == 7:
			word = word + 'seven'
		elif number == 8:
			word = word + 'eight '
		elif number == 9:
			word = word + 'nine'
		digit //= 10
		
	return word

	


toDo = 0	
while toDo != 5:
	toDo = printMenu()
	if toDo == 1:
		words = numtoWords()
		print words
	elif toDo == 2:
		num = wordstoNum()
		print num
	elif toDo == 3:
		print "Choice = 3"
	elif toDo == 4:
		print "Choice = 4"
	elif toDo == 5:
		print "Choice = 5"
	else:
		print "Wrong choice"
	

print "Bye!"
