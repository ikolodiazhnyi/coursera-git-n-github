def remove_punctuation(my_str):
	# define punctuation
	punctuations = '''!-[]{}();:'"\,<>./?@#$%^&*_~'''

	# remove punctuation from the string
	no_punct = ""
	for char in my_str:
		if char not in punctuations:
			no_punct = no_punct + char
	
	# return string without punctuation
	return no_punct


# display the unpunctuated string
print('The result of program is', remove_punctuation(input('Enter the string: ')))