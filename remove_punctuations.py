<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# define punctuation
punctuations = '''()-[]{};:'"\,<>./?!@#$%^&*_~'''
=======
=======
import socket

>>>>>>> 462fd39... Add simple network connectivity check
=======
>>>>>>> 5b0ca64... Revert "Add simple network connectivity check"
=======
import socket

>>>>>>> 8f64cbc... Revert "Revert "Add simple network connectivity check"
print('Program removes punctuation from the line you enter. Try this!')

def remove_punctuation(my_str):
	# define punctuation
	punctuations = '''!-[]{}();:'"\,<>./?@#$%^&*_~'''
>>>>>>> 5e3b0a8... Add explanation print

my_str = "Hello!!!, he said ---and went."

<<<<<<< HEAD
<<<<<<< HEAD
# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

<<<<<<< HEAD
# display the unpunctuated string
print(no_punct)
=======
=======
>>>>>>> 8f64cbc... Revert "Revert "Add simple network connectivity check"
def check_no_network():
	""" Returns True if it fails to resolve Google's URL, False otherwise"""
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True
<<<<<<< HEAD

# display the unpunctuated string
print('The result of program is', remove_punctuation(input('Enter the string: ')))
print(check_no_network())
>>>>>>> 72984be... Add simple network connectivity check
=======

# display the unpunctuated string
print('The result of program is', remove_punctuation(input('Enter the string: ')))
>>>>>>> 5b0ca64... Revert "Add simple network connectivity check"
=======

# display the unpunctuated string
print('The result of program is', remove_punctuation(input('Enter the string: ')))
print(check_no_network())
>>>>>>> 8f64cbc... Revert "Revert "Add simple network connectivity check"
