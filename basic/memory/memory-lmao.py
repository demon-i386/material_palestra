class Memoriakk:
	def add(self, number):
		number += 1;
		return number;

	def main(self):
		number = 666
		self.add(number)
		print("Numberokkkkkk ", number);
		number = self.add(number);
	
		print("Bolas!\nPython numeroskkkkkk: ", number)
cu = Memoriakk();
cu.main()

# Wtf????? cade as referencias??
# http://web.archive.org/web/20201111195827/http://www.effbot.org/zone/call-by-object.htm

# NÂOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOooo

# "call by assigment” VS "call by reference / Call by value? (ret)"
#   python		    C
