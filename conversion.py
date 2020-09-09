
class Obfuscate:
	class Name:
		pass
	
	class Content:
		pass

class _Obfuscate:
	default_key = "50156"
	@staticmethod
	def encode(txt = '', key = default_key):
		def normalize_encode(string):
			data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
			result = ""
			for s in string:
				q = ord(s)
				t = ""
				if q > len(data):
					t += data[len(data) - 1]
					t += data[q - (len(data) - 1)]
				else:
					t += data[q]
					t+= data[0]
				result += t
			return result
		
		universe = [c for c in (chr(i) for i in range(32, 127))]
		
		uni_len = len(universe)
		ret_txt = ''
		k_len = len(key)
		
		for i, l in enumerate(txt):
			if l not in universe:
				ret_txt += l
			else:
				txt_idx = universe.index(l)
				
				k = key[i % k_len]
				key_idx = universe.index(k)
				
				code = universe[(txt_idx + key_idx) % uni_len]
				
				ret_txt += code
		
		return normalize_encode(ret_txt)
	
	@staticmethod
	def decode(txt = '', key = default_key):
		
		def normalize_decode(string):
			data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
			result = ""
			index = 0
			t = 0
			for s in string:
				if index == 0:
					t += data.index(s)
					index = 1
				else:
					t += data.index(s)
					result += chr(t)
					index = 0
					t = 0
			return result
		
		txt = normalize_decode(txt)
		
		universe = [c for c in (chr(i) for i in range(32, 127))]
		uni_len = len(universe)
		ret_txt = ''
		k_len = len(key)
		
		for i, l in enumerate(txt):
			if l not in universe:
				ret_txt += l
			else:
				txt_idx = universe.index(l)
				
				k = key[i % k_len]
				key_idx = universe.index(k)
				key_idx *= -1
				
				code = universe[(txt_idx + key_idx) % uni_len]
				
				ret_txt += code
		
		return ret_txt

class XCPT:
	def __init__(self):
		pass
		
a = input()
print(_Obfuscate.encode(a))
print(_Obfuscate.decode(_Obfuscate.encode(a)))