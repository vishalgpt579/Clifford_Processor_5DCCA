#!/usr/bin/env python3

import clifford as cf
# from clifford import Cl
import numpy as np
from sympy import *
# Test case 
# V_bar = a0e0e4 + a1e1e4 + a2e2e4 + a3e3e4;
# S_bar = b0e0e3e4 + b1e1e3e4 + b2e2e3e4 + b3e4

class ALU:
	def __init__(self):
		
		self.loadTables()

	'''
	Function: 	loadTables(), Load Predefine Geometric Product results
	Input:		-
	Output:		bladeCoef, quadruples, geoProduct
	'''
	def loadTables(self):
		## Couple of ways to initials the Cl class object
		## 1st: E(3) --> CCl(5) : 3D CA to 5D CCA, problem with this is the symbols don't retain the sequence from zero.
		# layout, blades = Cl(3,names=['','e0', 'e1', 'e2', 'e01', 'e02','e12','e012'])
		# layoutc, bladesc, stuff = conformalize(layout)
		# locals().update(bladesc)
		# locals().update(stuff)

		## 2nd: Simple Cl(5) but with default sign, which is incorrect since the paper is refering to Minkowski Metric 
		# layout, blades = Cl(5,names=['','e0', 'e1', 'e2', 'e3', 'e4', 'e01', 'e02', 'e03', 'e04', 'e12', 'e13', 'e14', 'e23', 'e24', 'e34', 'e012', 'e013', 'e014', 'e023', 'e024', 'e034', 'e123', 'e124', 'e134', 'e234', 'e0123', 'e0124', 'e0134', 'e0234', 'e1234', 'e01234'], sig=[+1,+1,+1,+1,-1])
		# layout, self.blades = cf.Cl(5,names=['','e0', 'e1', 'e2', 'e3', 'e4', 'e01', 'e02', 'e03', 'e04', 'e12', 'e13', 'e14', 'e23', 'e24', 'e34', 'e012', 'e013', 'e014', 'e023', 'e024', 'e034', 'e123', 'e124', 'e134', 'e234', 'e0123', 'e0124', 'e0134', 'e0234', 'e1234', 'e01234'])
		
		## 3rd: Simple Cl(5) with names, sign/IDs
		self.layout, self.blades = cf.Cl(4,1,0,sig=[+1,+1,+1,+1,-1],firstIdx=0)
		

		globals().update(self.blades)

		# print('\nlocals() value inside class\n', locals())

		# self.bladeCoef = {
		# 0b000: 	{0b00001:"a0",0b00010:"a1",0b00100:"a2",0b01000:"a3"},
		# 0b001: 	{0b01110:"a123",0b01101:"a023",0b01011:"a013",0b00111:"a012"},
		# 0b010: 	{0b01001:"a03",0b01010:"a13",0b01100:"a23",0b0000:"1"},
		# 0b011: 	{0b00110:"a12",0b00101:"a02",0b00011:"a01",0b01111:"a0123"},
		# 0b100:	{0b10001:"a04",0b10010:"a14",0b10100:"a24",0b11000:"a34"},
		# 0b101:	{0b11110:"a1234",0b11101:"a0234",0b11011:"a0134",0b10111:"a0124"},
		# 0b110:	{0b11001:"a034",0b11010:"a134",0b11100:"a234",0b10000:"a4"},
		# 0b111:	{0b10110:"a124",0b10101:"a024",0b10011:"a014",0b11111:"a01234"}
		# }

		self.bladeCoef = {
		"V": 	np.asarray([0b00001,0b00010,0b00100,0b01000]),
		"T": 	np.asarray([0b01110,0b01101,0b01011,0b00111]),
		"S": 	np.asarray([0b01001,0b01010,0b01100,0b0000]),
		"P": 	np.asarray([0b00110,0b00101,0b00011,0b01111]),
		"V_bar":np.asarray([0b10001,0b10010,0b10100,0b11000]),
		"T_bar":np.asarray([0b11110,0b11101,0b11011,0b10111]),
		"S_bar":np.asarray([0b11001,0b11010,0b11100,0b10000]),
		"P_bar":np.asarray([0b10110,0b10101,0b10011,0b11111])
		}


		# self.quadruples = {
		# "V": 	["e0","e1","e2","e3"],
		# "T": 	["e1e2e3","e0e2e3","e0e1e3","e0e1e2"],
		# "S": 	["e0e3","e1e3","e2e3","1"],
		# "P": 	["e1e2","e0e2","e0e1","e0e1e2e3"],
		# "V_bar":["e0e4","e1e4","e2e4","e3e4"],
		# "T_bar":["e1e2e3e4","e0e2e3e4","e0e1e3e4","e0e1e2e4"],
		# "S_bar":["e0e3e4","e1e3e4","e2e3e4","e4"],
		# "P_bar":["e1e2e4","e0e2e4","e0e1e4","e0e1e2e3e4"]
		# }

		self.quadruples = {
		"V": 	[e0,e1,e2,e3],
		"T": 	[e123,e023,e013,e012],
		"S": 	[e03,e13,e23,1],
		"P": 	[e12,e02,e01,e0123],
		"V_bar":[e04,e14,e24,e34],
		"T_bar":[e1234,e0234,e0134,e0124],
		"S_bar":[e034,e134,e234,e4],
		"P_bar":[e124,e024,e014,e01234]
		}

		self.geoProduct = {
		"V": 	{"V":"S+P", "T":"S+P", "S":"V+T", "P":"V+T", "V_bar":"S_bar+P_bar", "T_bar":"S_bar+P_bar", "S_bar":"V_bar+T_bar","P_bar":"V_bar+T_bar"},
		"T": 	{"V":"S+P", "T":"S+P", "S":"V+T", "P":"V+T", "V_bar":"S_bar+P_bar", "T_bar":"S_bar+P_bar", "S_bar":"V_bar+T_bar","P_bar":"V_bar+T_bar"},
		"S": 	{"V":"V+T", "T":"V+T", "S":"S+P", "P":"S+P", "V_bar":"V_bar+T_bar", "T_bar":"V_bar+T_bar", "S_bar":"S_bar+P_bar","P_bar":"S_bar+P_bar"},
		"P": 	{"V":"V+T", "T":"V+T", "S":"S+P", "P":"S+P", "V_bar":"V_bar+T_bar", "T_bar":"V_bar+T_bar", "S_bar":"S_bar+P_bar","P_bar":"S_bar+P_bar"},
		"V_bar":{"V":"S_bar+P_bar", "T":"S_bar+P_bar", "S":"V_bar+T_bar", "P":"V_bar+T_bar", "V_bar":"S+P", "T_bar":"S+P", "S_bar":"V+T","P_bar":"V+T"},
		"T_bar":{"V":"S_bar+P_bar", "T":"S_bar+P_bar", "S":"V_bar+T_bar", "P":"V_bar+T_bar", "V_bar":"S+P", "T_bar":"S+P", "S_bar":"V+T","P_bar":"V+T"},
		"S_bar":{"V":"V_bar+T_bar", "T":"V_bar+T_bar", "S":"S_bar+P_bar", "P":"S_bar+P_bar", "V_bar":"V+T", "T_bar":"V+T", "S_bar":"S+P","P_bar":"S+P"},
		"P_bar":{"V":"V_bar+T_bar", "T":"V_bar+T_bar", "S":"S_bar+P_bar", "P":"S_bar+P_bar", "V_bar":"V+T", "T_bar":"V+T", "S_bar":"S+P","P_bar":"S+P"}
		}


	'''
	Function: 	result()
	Input:		multiplicand, multiplier, coeff of multiplicand, coeff of multiplier
	Output:		Extracted output from the Table-4 & Table 6
	'''
	def result(self,a,b,a_coeff,b_coeff):

		self.result_coeff=np.asarray([[a_coeff[0]*b_coeff[3] + a_coeff[3]*b_coeff[0],
							a_coeff[1]*b_coeff[3] + a_coeff[3]*b_coeff[1],
							a_coeff[2]*b_coeff[3] + a_coeff[3]*b_coeff[2],
							a_coeff[0]*b_coeff[0] + a_coeff[1]*b_coeff[1] + a_coeff[2]*b_coeff[2] + a_coeff[3]*b_coeff[3]],
							[a_coeff[1]*b_coeff[2]+a_coeff[2]*b_coeff[1],
							a_coeff[0]*b_coeff[2]+a_coeff[2]*b_coeff[0],
							a_coeff[0]*b_coeff[1]+a_coeff[1]*b_coeff[0],
							0]])

		mult_expression = self.geoProduct[a][b]
		# Extracting the expected results from the lookup-table.
		a_vec = np.sum(self.quadruples[mult_expression.split('+')[0]]*a_coeff)
		b_vec = np.sum(self.quadruples[mult_expression.split('+')[1]]*b_coeff)
		# print("type: ",type(self.result_coeff[0]))
		# quad_1 = np.sum(np.asarray(self.quadruples[mult_expression.split('+')[0]])*self.result_coeff[0])
		# quad_2 = np.sum(np.asarray(self.quadruples[mult_expression.split('+')[1]])*self.result_coeff[1])

		# print("a_vec: ",quad_1)
		# print("b_vec: ",quad_2)
		# print("1st_quad_coeff: ",self.result_coeff[0])
		# print("2nd_quad_coeff: ",self.result_coeff[1])
		# output = quad_1+quad_2

		output = a_vec+b_vec
		# output = np.sum(self.quadruples[mult_expression.split('+')[0]]+self.quadruples[mult_expression.split('+')[1]])
		return(mult_expression, output)

	def GeoProd(self,a,b):
		# Take the XOR between blade coeff masks to get the mask of the output blade.
		# multiply quadruples using Minsowki metric to get the sign

		# sign = np.empty([1,16])
		# a_vec = self.quadruples[a]
		# b_vec = self.quadruples[b]
		a_coeffs = np.asarray(self.bladeCoef[a])
		b_coeffs = np.asarray(self.bladeCoef[b])


		# sign = np.sign(a_vec*b_vec) #Doing this defeats the purpose
		# print(sign)

		a_xor_b = np.bitwise_xor(b.reshape([4,1]),a.reshape([1,4]))

	'''
	Function: 	CLMul()
	Input:		multiplicand, multiplier, coeff of multiplicand, coeff of multiplier
	Output:		Explicit Geometric multiplication of multiplicand & multiplier
	'''
	def CLMul(self,a,b,a_coeff,b_coeff):

		a_vec = np.sum(self.quadruples[a]*a_coeff)
		b_vec = np.sum(self.quadruples[b]*b_coeff)
		print(a,"=",a_vec)
		print(b,"=",b_vec)
		# print("Value of a now: ",a)
		# print("Value of b now: ",b)
		# print("Value of a as vec: ",a_vec)
		# print("Value of b as vec: ",b_vec)

		c = cf.np;
		print("\n\nExplicit Mulitplication...")
		c = np.asarray(a_vec)*np.asarray(b_vec)
		print("Value:\n",c)

		## Uncomment the below to see the geometric product happening in sequence
		# e = 0
		# print("\n\nMultiplying using for loop...\n")
		# for i in a:
		# 	for j in b:
		# 		print("\nValue of i: ",i," \t","Value of j: ",j)
		# 		# e +=(i^j)+(i|j)
		# 		e += (i*j)
		# 		print(i," outerproduct ",j,"= ",(i^j))
		# 		print(i," innerproduct ",j,"= ",np.multiply(i,j))
		# 		print("Geometric Product: ",e)

		# c_coeff = [eval(i) for i in list(filter(None,c.split('e')))]

		return c

	def test(self):
		print("working.")
