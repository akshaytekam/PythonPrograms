"""
   * author - Akshay Tekam
   * date - 10/01/2021
   * time - 11:22:56
   * package - ${PACKAGE_NAME}
   * Title - Computes the prime factorization of N .
"""

class Factor:
    # By taking the number from user and
    # calculating the factor
    def primeFactor(self):
        number = int(input("Enter a number: "))
        factors = []

        while number % 2 == 0:
            factors.append(2)
            number //= 2

        divisor = 3
        while number != 1 and divisor <= number:
            if number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            else:
                     # prime numbers add except 2.
                divisor += 2
        print("The prime factors are:")
        for i in range(len(factors)):
            print(factors[i], end=' ')
obj=Factor()
obj.primeFactor()
