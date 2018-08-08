# Hi,
# This photo has a message embedded in it.
# As a hint, I have given the code of how I have encoded it.
# I have also defined all the functions that you will need to decode the image
# You just need to come up with the logic of decoding it.
# It is your job to complete the unhide() function.
# Sorry if this is too tough/easy for you :P I have never set questions for anyone before
# If you want I can just send you the solution! :)

# General intructions:
# 0) Download and install PIL :P
#    Don't worry you don't need to know anything about PIL. That part is already taken care of

# 1) Start following the code from if __name__ == '__main__' block (meh you already know this)
#    The first three lines which are commented out show how I used the hide() function to encode the message

# 2) You only need to write a part of unhide().
#    Use the functions defined in functions.py to help you out.
#    You won't need to define any other functions

# 3) This is not any standard encryption algorithm. I don't even think this can be classified as encryption.
#    Don't waste time thinking about what you studied in crypto class. Unless you studied 'Steganography'.
#    Don't worry though; it is not a standard encryption algorithm for a reason: It is extremely easy to decode :P
#    Hint: Think about pixel manipulation :)
#    The hash function is only used to check if you have decoded the full/correct message
#    You won't be able to decode the message using any function in the Crypto/hashlib library.
# 	 Just use the functions I have already defined

# I have almost written the unhide function as well :P
# You just have to write 3 lines of code :P

# Happy birthday Nidhz!

from PIL import Image
import functions			# Use the functions inside this file. You will need only these functions

import sanity_check		# This will be of no use to you
						# This is just for me to check if you have decoded the correct/complete messsage :)

def encode(hexcode, digit):
	hexcode = hexcode[:-1] + digit		# Hint: This changes LSB of every pixel
	return hexcode

def decode(hexcode):
		return hexcode[-1]


def hide(filename, message):
	img = Image.open(filename) # Meh
	binary = functions.str2bin(message) + '1111111111111110' # 1111111111111110 bit pattern marks the end of the message
												   # So suppose I want to store 'blah' the binary version will be: '11000100110110001100001011010001111111111111110'
												   # ie: the last 16 bits will always be 1111111111111110
	img = img.convert('RGBA')
	if img.mode in ('RGBA'):					   # Sanity check

		data = img.getdata()					   # list of tuples containing RGB values as its first three elements

		newData = []							   # Modidified image pixels

		digit = 0
		temp = ''
		for item in data:
			if (digit < len(binary)):
				newpix = encode(functions.rgb2hex(item[0],item[1],item[2]),binary[digit])   # item[0], item[1], item[2] correspond to the RGB values
																				  # encode will only return data if some condition is met
				r, g, b = functions.hex2rgb(newpix)
				newData.append((r,g,b,255))
				digit += 1
			else:
				newData.append(item)

		img.putdata(newData)						# Overwriting image with new pixels
		img.save(filename, "PNG")
		return True

	return False




def unhide(filename):
	img = Image.open(filename)
	binary = ''    						# binary will store the decoded message in binary form

	img = img.convert('RGBA')
	if img.mode in ('RGBA'):			# Sanity check
		data = img.getdata()

		for item in data:
			hidden_digit = decode(functions.rgb2hex(item[0],item[1],item[2]))

			# Remove the print statement
			# Store the retrieved data in a string
			# Return the string from here
			# return "Write your code here and remove this line"
			binary = binary + hidden_digit
			if (binary[-16:] == '1111111111111110'):
				return functions.bin2str(binary[:-16])



	else:
		return False


if __name__ == '__main__':
	# For hiding data
	# fh = open('text.txt', 'r')
	# s = fh.read()
	# hide_check = hide('budday.png', s)

	# The part that you have to write:
	# Return the entire message as a single string
	s = unhide('budday.png')

	# You don't need to change this. This is for me to check if you got it right
	if s is not False and sanity_check.check(s):
		print s
	elif s is False:
		print "bapchufied: Something went wrong from the start"
	else:
		print "bapchufied: Wrong/incomplete message decoded"

	# fh.close()
