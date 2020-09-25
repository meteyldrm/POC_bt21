import bitstring, io, os

class PathProc:
	@staticmethod
	def resolve(path):
		if len(path) > 255:
			path = "\\\\?\\" + path
		return path

class BiProc:
	"""Binary processor for SEPS-like applications"""
	def __init__(self, root):
		self.root = root
		self.major = -1
		self.minor = -1
		if os.path.isfile(PathProc.resolve(root)):
			self.checkSEPSCompatibility()
			
	def checkSEPSCompatibility(self):
		with open(self.root, "rb") as file:
			byte = file.read(1)
			if byte:
				data = bitstring.BitArray(byte).bin
				self.major = int("000"+data[:5], 2)
				self.minor = int("00000"+data[5:], 2)
			print("SEPS version " + str(self.major) + "." + str(self.minor))
			
class b:
	def __init__(self):
		pass

class f(b):
	pass

class d(f):
	pass

with open("a.seps", "wb+") as f:
	f.write(bytes(b"\x05"))
	
p = BiProc("a.seps")