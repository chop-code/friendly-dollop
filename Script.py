import numpy as numpy

degree = int(input("Degree:"))
coeffs = []

for c in range (0,degree+1):
        coefficient = int(input("number: "))
        coeffs.append(coefficient)
        #print(coeffs)        

p = numpy.poly1d(coeffs)
print(p)
roots = p.roots
print("Roots:", roots)
Exit = input("PRESS ANY BUTTON TO EXIT")