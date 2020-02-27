# calculer le volume d'un parallellepipede formé par 3 vecteurs donné sous la forme de liste python [x,y,z]
#

def volume(A,B,C):
	import numpy as np 
	a = np.array(A)
	b = np.array(B)
	c = np.array(C)
	cross = np.cross(b,c)
	vol = np.vdot(a,cross)
	return vol

A = [1,2,0]
B = [0,8,3]
C = [1,1,1]
print(volume(A,B,C))