import string, json

class languagestring(object):
	def __init__(self):
		self.string = string

		with open('assets/language_detailed.json','r') as f:
			self.language_dict = json.load(f)
			f.close()


	def language_string(self,language):
		return ''.join(ls.language_dict[language]['lowercase']['letter'])



if __name__ == "__main__":
	ls = languagestring()
	print(ls.string.ascii_lowercase)
	print(ls.language_string('cz'))