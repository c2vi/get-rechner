
##Imports------------------------------------------
from os import listdir,path
from time import time
from numba import njit
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sympy as sp



'''
Converts T to Pi Circuit Topology Symbolically

from sympy import simplify, Symbol, pprint, collect_const

 # Use this for your imaginary symbol
j = Symbol('j')

# Circuit symbols
R = Symbol('R')
w = Symbol('w')
L = Symbol('L')
C = Symbol('C')

# Arbitrary Circuit Element Equations
R1 = 1 / (j*w*C)
R2 = R + j*w*L
R3 = R + j*w*L

# Circuit conversion equations
RN = R1 * R2 + R2 * R3 + R1 * R3 
RA = RN / R1
RB = RN / R2
RC = RN / R3

#Print the original circuit element equations
pprint(R1)
print("\n")
pprint(R2)
print("\n")
pprint(R3)

#Print the original solved equation, followed by the appropriately reduced equation
print("\nOriginal\t")
pprint(RA)
print("\nReduced\t")
pprint(collect_const(simplify(RA),j))

print("\nOriginal\t")
pprint(RB)
print("\nReduced\t")
pprint(collect_const(simplify(RB),j))

print("\nOriginal\t")
pprint(RC)
print("\nReduced\t")
pprint(collect_const(simplify(RC),j))

'''

g1 = "3x-8y+4"
g2 = "2x-9y+1"




