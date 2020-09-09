import os
from enum import Enum
from bitstring import BitArray, Bits

class PathEnum(Enum):
	INVALID = 0
	FILE = 1
	FOLDER = 2

def validate_path(path) -> PathEnum:
	if os.path.isfile(path):
		return PathEnum.FILE
	elif os.path.isdir(path):
		return PathEnum.FOLDER
	else:
		return PathEnum.INVALID
	
class Binary:
	@staticmethod
	def encode_bitstring(data): #Convert utf-8 string to the binary representation
		byte_object = str(data).encode('utf-8')
		hex_object = byte_object.hex()
		return BitArray(hex=hex_object).bin
	
	@staticmethod
	def decode_bitstring(data): #Binary to utf-8 string
		return (bytes.fromhex(BitArray(bin=data).hex)).decode('utf-8')
	
	def encode_codepoint(self, data): #utf-8 code point to 21-bit string
		#The last 2 bits are used to determine how many bits there were before padding
		index = 0
		binary = ""
		d = self.encode_bitstring(data)
		for c in d:
			if index == 0 and c == 0:
				return d[1:].ljust(21, "0")
			if c == "1":
				index += 1
			elif c == "0":
				binary += d[(index+1):8]
				n = 0
				m = 0
				for i in d:
					if m == 8:
						n += 1
						m = 0
					if n == 0:
						if m > index:
							binary += i
					else:
						if m > 1:
							binary += i
					m += 1
				temp = binary.ljust(19, "0")
				if index == 0:
					index = 1
				bits = Bits(uint=index, length = 2)
				temp += bits.bin
				return temp
			
	@staticmethod
	def decode_codepoint(self, data):
		bit = data[-2:0]
		print("data " + data)
		print("bit " + str(bit))
		length = Bits(bin=bit).uint
		codepoint = ""
		for n in range(0, length):
			print("n equals " + str(n))
	
b = Binary()
b.decode_bitstring(b.decode_codepoint(b, b.encode_bitstring(b.encode_codepoint("a"))))

class Path:
	class Name:
		def encode(self, string):
			pass
		
		def decode(self):
			pass