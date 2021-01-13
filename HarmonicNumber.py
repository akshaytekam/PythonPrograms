"""
   * author - Akshay Tekam
   * date - 10/01/2021
   * time - 11:45:23
   * package - ${PACKAGE_NAME}
   * Title - Prints the Nth harmonic number
"""
class Harmonic:
    # take a number of harmonic function.
    def nthHarmonic(self):
        harmonic = 1.00
        N = int(input("Enter a number: "))

        for i in range(2, N + 1):
            harmonic += 1 / i

        return harmonic

obj=Harmonic()
print(obj.nthHarmonic())

