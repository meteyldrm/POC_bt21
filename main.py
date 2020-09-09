"""
Disclaimer: the initial commit content was written with a nonzero blood alcohol concentration.

Unrelated hypothesis: For every text there exists an algorithm such that the hash of the data is the summary of the text itself.

Every directory and its contents can be read in binary and converted to encoded text. Local data length declaration with length flags
will be used for hierarchy reconstruction while the metadata will be stored in a dictionary. Note for future development: SEPS v3 BLD doesn't account for flags and has
significant overlap in the lower bounding regions. SEPS v4 is devised such that the growth function remains the same except for bit-level transmission.

Another unrelated hypothesis: Lossy and even losslessly compressed data may be decompressed by humans
if barely-recognizable text can be created by a short seed that will eventually result in the recovery of full data.

A node is shared for every entry in a directory, therefore the bitwise shift of one value is sufficient for hierarchy reconstruction.
The remaining entries may be shifted to provide low-value deltas.
"""

import bitstring

def length_initializer(binaryData, depth=0):
	length = len(binaryData)
	a = 0
	b = 0
	c = 0
	
	"""
	a(2^i)x + b(2^(i+7))x + c(2^(i+31))x + ...
	"""
	result = bitstring.BitArray()
	
	if depth >= 0:
		while a**2 < length:
			a += 1
		if depth == 0:
			for _ in range(a):
				result.append(True)
			result.append(False)
	if depth >= 1:
		while (b + 7)**2 < length:
			b += 1
		if depth == 1:
			result.append(False)
			for _ in range(b):
				result.append(True)
			result.append(False)
	if depth >= 2:
		while (c + 31)**2 < length:
			c += 1
		if depth == 2:
			result.append(False)
			result.append(False)
			for _ in range(c):
				result.append(True)
			result.append(False)