"""
   * author - Akshay Tekam
   * date - 11/01/2021
   * time - 05:04:02
   * package - math, sqrt
   * Title - find the roots of the equation
      a*x*x+b*x+c
"""
from math import sqrt
class Quadratic:
    # taking the value of a b and c and
    # putting into equation r.
    def findRoots(self):
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        r = b ** 2 - 4 * a * c

        if r > 0:
            num_roots = 2
            x1 = (((-b) + sqrt(r)) / (2 * a))   # first root
            x2 = (((-b) - sqrt(r)) / (2 * a))   # second root
            print("There are 2 roots: %f and %f" % (x1, x2))
        elif r == 0:                          # condition of no roots
            num_roots = 1
            x = (-b) / 2 * a
            print("There is one root: ", x)
obj=Quadratic()
obj.findRoots()           # create object and calling it

