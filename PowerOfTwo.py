"""
   * author - Akshay Tekam
   * date - 10/01/2021
   * time - 02:05:22
   * package - ${PACKAGE_NAME}
   * Title - This program takes a command-line argument N and prints a table of thepowers of 2 that are less than or equal to 2^N.
"""
class Power:
    def powerOfTwo(self):
        number = int(input("Enter a number: "))
        i = 0
        while i <= number:
            print(pow(2, i))
            i += 1
obj=Power()
obj.powerOfTwo()

