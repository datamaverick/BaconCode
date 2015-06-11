import index
from sys import exit

#input the message to encrypt, remove space and evaluate its type
user_input = raw_input("Enter the message here: ").lower()
inter_list = index.remove_space(user_input)

if not all(i.isalpha() for i in inter_list):
	print("Please enter only alphabetical letters")
	exit(0)

#assigns a number to each letter
num_list = [index.inv_alphabets[x] for x in inter_list]

#return the binary representation of each number in the list
binary_list = [index.inv_numbers[x] for x in num_list]

#get the list of letters a and A
format_list = index.assign_letter(binary_list)

letter_count = len(format_list)
print("You need to create a message with %d letters" %(letter_count))
msg_input = raw_input("So what message are you thinking?\n > ")

#evaluate the length of the message.
temp_list = index.remove_space(msg_input)
while len(temp_list) != letter_count:
	print("The total characters must be %d" %(letter_count))
	msg_input = raw_input("Please re-enter a valid message\n > ")
	temp_list = index.remove_space(msg_input)

#position is a list that contains the indices of letters that need to be capitalized in the message
position = index.position_list(format_list)

encrypt_str = "".join(c.upper() if i in position else c for i, c in enumerate(temp_list))
print("Your encrypted message is: %s" %(encrypt_str))








