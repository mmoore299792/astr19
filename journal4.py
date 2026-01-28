# Write an initialization function that sets the values of the 
#data members when an instance of the class is created

#Write a member function of the class to print out and describe 
#the data members representing the physical characteristics of the animal.

class animal:
	def __init__(self,armlength,leglength,eyenumber,has_tail,is_furry):
		self.armlength = armlength
		self.leglength = leglength
		self.eyenumber = eyenumber
		self.has_tail = has_tail
		self.is_furry = is_furry

	def describe(self):
		print(f"Attributes of the cat")
		print(f"Arm length (in): {self.armlength}")
		print(f"Leg length (in): {self.leglength}")
		print(f"Number of eyes: {self.eyenumber}")
		print(f"Has tail: {self.has_tail}")
		print(f"Is furry: {self.is_furry}")

cat = animal(9,10,2,True,True)

cat.describe()