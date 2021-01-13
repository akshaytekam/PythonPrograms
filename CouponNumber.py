"""
   * author - Akshay Tekam
   * date - 12/01/2021
   * time - 11:44:45
   * package - ${PACKAGE_NAME}
   * Title - Given N distinct Coupon Numbers, how many random numbers
    do you need to generate distinct coupon number.
"""
from itertools import permutations
import random
import string
# generating random coupon of given staring
# and find all possible permutations.
def randomGeneration(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))         # generate random value
ini_str = "abcdefghijklmnopqrst"

N=int(input("Enter length of coupon: "))
permutation = [''.join(p) for p in permutations(randomGeneration(N, ini_str))]      # generate permutations
print("Resultant List", str(permutation))
print("to generate distinct coupon of length "+ str(N)+ " we need "+ str(len(permutation)) + " more coupons")











