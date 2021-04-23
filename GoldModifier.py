import numpy as np
import matplotlib.pyplot as plt
def ArmyEstimator(modifier):
	x=list(range(10, 3000, 10))
	x.sort()
	y=list()
	for i in x:
		army=0
		z=1
		while i>=modifier*z:
			i-=modifier*z
			army+=modifier
			z+=1
		army+=int(i/z)
		i=int(i/z)
		y.append(army)

	plt.plot(x, y, 'bo')
	plt.show()

#ArmyEstimator()
#to use program, use above statement with hashtag deleted and with the modifier placed in the parentheses