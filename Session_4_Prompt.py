class Fav_Animal:

	def __init__(self,arm_length,leg_length,
		num_eyes,tail=False,furry=False):
		self.arm_length = float(arm_length)
		self.leg_length = float(leg_length)
		self.num_eyes = int(num_eyes)
		self.tail = tail
		self.furry = furry

	def describe(self):
		print(f"My favorite animal's arms are {self.arm_length} inches long.")
		print(f"Its legs are {self.leg_length} inches long.")
		print(f"This animal has {self.num_eyes} eyes.")

		if self.tail == True:
			print("It has a tail.")
		else:
			print("It doesn't have a tail.")

		if self.furry == True:
			print("It's furry!")
		else:
			print("It's not furry.")




def main():
	my_fav_animal = Fav_Animal(8.5, 8, 2, True, True)

	my_fav_animal.describe()


if __name__=="__main__":
	main()