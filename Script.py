#import the numpy module
import numpy as numpy

#Ask user for degree of polynomial
degree = int(input("Degree:"))

#create a list called 'coeffs'
coeffs = []

#iterate the degree + 1 times, asking for the coefficient of each degree.
for c in range (0,degree+1):
        coefficient = int(input("number: "))
        
        #append the inputs to the 'coeffs' list created on line 8
        coeffs.append(coefficient)
               
#Put coefficients in the form of a polynomial
p = numpy.poly1d(coeffs)
print(p)

#Use numpy to calculate roots
roots = p.roots

#Output the result
print("Roots:", roots)
Exit = input("PRESS ANY BUTTON TO EXIT")