'''
Triangular, pentagonal, and hexagonal
Problem 45 
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.


Answer:
1533776805
Completed on Fri, 29 Dec 2017, 14:17

'''

from math import sqrt

def pentagonNumberToN(num):
	return ( 0.5 + sqrt(0.25 + 6 * num )) / 3 

def hexagonalNumberToN(num):
	return ( 1 + sqrt ( 1 + 8 * num)) / 4

def nToTriangleNumber(num):
	return ( num * num + num) / 2

i = 28

while(True):
	tempI = i
	i += 1
	'''
	if ( tempI % 100000 == 0):
		print("current i... %d" % (tempI))
	'''
	Ti = nToTriangleNumber(tempI)
	Hi = hexagonalNumberToN(Ti)
	Pi = pentagonNumberToN(Ti)


	if Hi != int(Hi) or Pi != int(Pi):
		continue

	print("i: %d, Ti: %d, Hi: %d, Pi: %d" % (tempI, Ti, Hi, Pi))