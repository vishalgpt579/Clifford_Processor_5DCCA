#!/usr/bin/env python3

import CliffALU5 as cl 	# CliffALU5 Emulation
import clifford as cf 	# arthimetics of clifford algebra
import numpy as np

# def init_cliffALU():
# 	alu = cl.ALU()
# 	alu.loadTables() #Load the tables

# 	#Load the quadruples table
# 	quadTable = alu.quadruples
# 	#Load the geometric product table
# 	prodTable = alu.geoProduct
# 	#Load the coefficient table
# 	coefTable = alu.bladeCoef

def main():
	# Initialising 32-blades for 5D Geometric-Algebra space &
	# lookup-table for CliffALU5
	alu = cl.ALU()

	a = 'V'
	b = 'V'
	a_coeff = np.asarray([1,1,1,1])
	b_coeff = np.asarray([1,1,1,1])

	print("Testing CLMul(Geometric Product)... between ",a," & ",b,"...")
	c_obtained = alu.CLMul(a,b,a_coeff,b_coeff)
	print("\n\nResults from Explicit Geometric Multiplication: ",c_obtained)

	# Using lookup for getting the expected results...
	c_expected_exp,c_expected_op = alu.result(a,b,a_coeff,b_coeff)
	print("\n\nExpected result from Lookup-Tables, i.e \n",a,"*",b,"= ",c_expected_exp,"=",c_expected_op)


	print("\n\nChecking if the results matches, by computing their outer product...")
	res = ((c_obtained)^(c_expected_op))
	if res==0:
		print("Yes !!")
	else:
		print("No :(")
		print("\nSince the outer product of should be zero, but it is...\n",res)

	alu.GeoProd(a,b)




'''
>>> a_coeff = np.array([1,2,1,2])
>>> a_vec = a*a_coeff
>>> a_vec
array([(1^e04), (2^e14), (1^e24), (2^e34)], dtype=object)
>>> a_vec = np.sum(a_vec)
>>> a_vec
(1^e04) + (2^e14) + (1^e24) + (2^e34)
>>> b_coeff = np.array([2,1,2,1])
>>> b_vec = b*b_coeff
>>> b_vec
array([(2^e034), (1^e134), (2^e234), (1^e4)], dtype=object)
>>> b_vec = np.sum(b_vec)
>>> b_vec
(1^e4) + (2^e034) + (1^e134) + (2^e234)
>>> a_vec
(1^e04) + (2^e14) + (1^e24) + (2^e34)
>>> b_vec
(1^e4) + (2^e034) + (1^e134) + (2^e234)
>>> 
>>> 
>>> (a_vec)*(b_vec)
-(3^e0) - (3^e2) + (8^e3) - (3^e013) + (3^e123)
>>> resultant_coeff = [[a_coeff[0]*b_coeff[3]+a_coeff[3]*b_coeff[0],\
...                     a_coeff[1]*b_coeff[3]+a_coeff[3]*b_coeff[1],\
...                     a_coeff[2]*b_coeff[3]+a_coeff[3]*b_coeff[2],\
...                     a_coeff[0]*b_coeff[0]+a_coeff[1]*b_coeff[1],a_coeff[2]*b_coeff[2]+a_coeff[3]*b_coeff[3]],\
...                     [a_coeff[1]*b_coeff[2]+a_coeff[2]*b_coeff[1],\
...                     a_coeff[0]*b_coeff[2]+a_coeff[2]*b_coeff[0],\
...                     a_coeff[0]*b_coeff[1]+a_coeff[1]*b_coeff[0],\
...                     0]]]
'''


if __name__ == '__main__':
	main()