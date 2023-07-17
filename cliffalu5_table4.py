#!/usr/bin/env python3

import CliffALU5 as cl 	# CliffALU5 Emulation
import clifford as cf 	# arthimetics of clifford algebra
import numpy as np
from sympy import *

## Defining CL(4,1,0)
layout, blades = cf.Cl(4,1,0,sig=[+1,+1,+1,+1,-1],firstIdx=0)
locals.update(blades)

## Defining Table2, multivector
quadruples = {
		"V": 	[e0,e1,e2,e3],
		"T": 	[e123,e023,e013,e012],
		"S": 	[e03,e13,e23,1],
		"P": 	[e12,e02,e01,e0123],
		"V_bar":[e04,e14,e24,e34],
		"T_bar":[e1234,e0234,e0134,e0124],
		"S_bar":[e034,e134,e234,e4],
		"P_bar":[e124,e024,e014,e01234]
		}

## defining symbols
(a0,a1,a2,a3) = symbols("a0 a1 a2 a3")
(b0,b1,b2,b3) = symbols("b0 b1 b2 b3")

