print('Program removes punctuation from the line you enter', end='')
print(' and tells if it fails to resolve Google\'s URL')

import socket

# define punctuation
punctuations = '''()-[]{};:'"\,<>./?!@#$%^&*_~'''

def remove_punctuation(my_str):
	# define punctuation
	punctuations = '''!-[]{}();:'"\,<>./?@#$%^&*_~'''

def remove_punctuation(my_str):
	# remove punctuation from the string
	no_punct = ""
	for char in my_str:
		if char not in punctuations:
			no_punct = no_punct + char
	# return string without punctuation
	return no_punct

def check_no_network():
	""" Returns True if it fails to resolve Google's URL, False otherwise"""
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True


# display the unpunctuated string
print('The result of program is', remove_punctuation(input('Enter the string: ')))
print('Fails to resolve Google\'s URL -', check_no_network())