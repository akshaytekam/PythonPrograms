"""
   * author - Akshay Tekam
   * date - 11/01/2021
   * time - 10:25:33
   * package - ${PACKAGE_NAME}
   * Title - A 2D arrays of integers, doubles, or booleans from
     standard input and printing them out to standard output.
"""
from numpy import *
class TwoDyArray:
    # taking the column and row size and
    # putting them into array
    def arrayInput(self):
        r=int(input("Enter row size:"))
        c=int(input("Enter col size:"))
        array=zeros((r, c), dtype=int)
        size=len(array)

        for i in range(size):                    # Taking elements
            for j in range(len(array[i])):
                x=int(input("Enter Element:"))
                array[i][j]=x

        for i in range(size):
            for j in range(len(array[i])):
                print(array[i][j])               # Print the elements.
        print(array)
obj=TwoDyArray()
obj.arrayInput()

