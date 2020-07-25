<<<<<<< HEAD
# define punctuation
punctuations = '''()-[]{};:'"\,<>./?!@#$%^&*_~'''
=======
print('Program removes punctuation from the line you enter. Try this!')

def remove_punctuation(my_str):
	# define punctuation
	punctuations = '''!-[]{}();:'"\,<>./?@#$%^&*_~'''
>>>>>>> 5e3b0a8... Add explanation print

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)