#	Name: Akshay Kumar Singh
#	Objective: A woman has n colors of bangles of 2 count each. She wants to put the same arrangement of
#   bangles on both of her hands. She can put 1 to n bangles arrangement, with both hands having the same arrangement.
#   What are the different ways in which she can choose the bangles?
#	Date Modified: 12-07-2018
#	Time complexity: O(n)
#	Space complexity: O(1)


class Bangles:
	def __init__(self, numberOfColors):
		self.numberOfColors = numberOfColors

	def arrange(self):
		factorial = 1
		for color in range(1, self.numberOfColors+1):
			factorial *= color
		return(factorial*2)

numberOfColors = 4
bangleObject = Bangles(numberOfColors)
print(bangleObject.arrange())
