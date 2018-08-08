import binascii

def rgb2hex(r, g, b):
	"""
	>>> rgb2hex(14, 200, 64)
		'#0ec840'
	"""
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
	"""
	>>> hex2rgb('#0ec840')
	(14, 200, 64)
	"""
	return tuple(map(ord, hexcode[1:].decode('hex')))

def str2bin(message):
	"""
	>>> str2bin('blah')
	'1100010011011000110000101101000'
	"""
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]

def bin2str(binary):
	"""
	>>> bin2str('1100010011011000110000101101000')
	'blah'
	"""
	message = binascii.unhexlify('%x' % (int('0b'+binary,2)))
	return message
