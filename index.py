#Dictionary 1 for conversion of binary representation to regular numbers
numbers = {
	'00000': '0', '00001': '1', '00010': '2', '00011': '3', '00100': '4', '00101': '5',
	'00110': '6', '00111': '7', '01000': '8', '01001': '9', '01010': '10', '01011': '11',
	'01100': '12', '01101': '13', '01110': '14', '01111': '15', '10000': '16', '10001': '17',
	'10010': '18', '10011': '19', '10100': '20', '10101': '21', '10110': '22', '10111': '23',
	'11000': '24', '11001': '25'
}

#Dictionary 2 for index of letters in the alphabets
alphabets = {
	'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g',
	'7': 'h', '8': 'i', '9': 'j', '10': 'k', '11': 'l', '12': 'm',
	'13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's',
	'19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z'
}

#input the message to decode
user_input = raw_input("Enter the code here: ")
test_list = list(user_input)
temp_list = [s for s in test_list if s != " "]  #list of characters from input bar spaces
if len(temp_list) % 5 != 0:
	print("The total characters must be multiples of 5 for Bacon codes")
	user_input = raw_input("Enter the code here: ")

#Assign values of 1 or 0 based on uppercase or lowercase letters and store in temp_list
for n,letter in enumerate(temp_list):
	if letter.isupper():
		temp_list[n] = '1'
	else:
		temp_list[n] = '0'

#num_list stores binary representation, in groups of 5 numbers each.
num_list = []
k = 0
while k < (len(temp_list)):

	newitem = ''.join(temp_list[k:k+5])
	num_list.append(newitem)
	k +=5
#print(num_list)

inter_list = [numbers[x] for x in num_list]
#print(inter_list)

decode_list = [alphabets[x] for x in inter_list]

print "The hidden message is:"
print(decode_list)






