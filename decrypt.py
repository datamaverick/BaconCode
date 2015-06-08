import index

#input the message to decode and evaluate its length
user_input = raw_input("Enter the code here: ")

temp_list = index.remove_space(user_input)
while len(temp_list) % 5 != 0:
	print("The total characters must be multiples of 5 for Bacon codes")
	user_input = raw_input("Enter the code here: ")
	temp_list = index.remove_space(user_input)

index.assign_number(temp_list)

num_list = index.binary_rep(temp_list)

try: 
	""" To handle mistyping of upper/lowercase letters, which won't find a key
	in the dictionary
	"""
	#look up in corresponding dictionaries and store results in the lists
	inter_list = [index.numbers[x] for x in num_list]

	decode_list = [index.alphabets[x] for x in inter_list]

	print "The hidden message is:"
	print(decode_list)

except KeyError:
	print("You mistyped an upper or lower case letter")
	exit