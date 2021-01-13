"""
   * author - Akshay Tekam
   * date - 10/01/2021
   * time - 11:23:34
   * package - ${PACKAGE_NAME}
   * Title - Flip Coin and print percentage of Heads and Tails
"""
import random
class FlipCoin:
    # By using random function identify heads or tails
    def flip(self):

        flips = int(input("Enter number of flips: "))
        heads = 0
        tails = 0
        for i in range(flips):
            coin = random.randint(0, 1)
            if coin < 0.5:
                tails += 1
            else:
                heads += 1
        # Percentage of head and tail.
        percentOfTail = (tails * flips) / 100
        print(percentOfTail)
        percentOfHead = (heads * flips) / 100
        print(percentOfHead)
obj=FlipCoin()
obj.flip()