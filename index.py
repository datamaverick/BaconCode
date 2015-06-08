#Dictionary 1 for conversion of binary representation to regular numbers
numbers = {
	'00000': '0', '00001': '1', '00010': '2', '00011': '3', '00100': '4', '00101': '5',
	'00110': '6', '00111': '7', '01000': '8', '01001': '9', '01010': '10', '01011': '11',
	'01100': '12', '01101': '13', '01110': '14', '01111': '15', '10000': '16', '10001': '17',
	'10010': '18', '10011': '19', '10100': '20', '10101': '21', '10110': '22', '10111': '23',
	'11000': '24', '11001': '25'
}

#Dictionary 2 for reverse lookup of dictionary 1
inv_numbers = {v: k for k, v in numbers.items()}

#Dictionary 3 for index of letters in the alphabets
alphabets = {
	'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g',
	'7': 'h', '8': 'i', '9': 'j', '10': 'k', '11': 'l', '12': 'm',
	'13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's',
	'19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z'
}

#Dictionary 4 for reverse lookup of dictionary 1
inv_alphabets = {v: k for k, v in alphabets.items()}

def remove_space(msg):
#remove the spaces from the input messages and return characters in a list
	test_list = list(msg)
	results = [s for s in test_list if s != " "]
	return results

def assign_number(ls):
#Assign values of 1 or 0 based on uppercase or lowercase letters
	for n,letter in enumerate(ls):
		if letter.isupper():
			ls[n] = '1'
		else:
			ls[n] = '0'
	return ls

def binary_rep(old_list):
#new_list stores binary representation, in groups of 5 numbers each.
	new_list = []
	k = 0
	while k < (len(old_list)):

		newitem = ''.join(old_list[k:k+5])
		new_list.append(newitem)
		k +=5
	return new_list

def assign_letter(binary_list):
#convert the binary values of 0 and 1 to letters a and A and store in a list
	sep = ''
	temp_msg1 = sep.join(binary_list)
	temp_msg2 = temp_msg1.replace('0','a')
	temp_msg = temp_msg2.replace('1','A')

	format_list = list(temp_msg)
	return format_list

def position_list(format_list):
	position = []
	i = 0
	while i < (len(format_list)):
		if format_list[i].isupper() == True:
			position.append(i)
		i += 1

	return position


