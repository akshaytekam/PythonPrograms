"""
   * author - Akshay Tekam
   * date - 12/01/2021
   * time - 11:44:45
   * package - ${PACKAGE_NAME}
   * Title - Given N distinct Coupon Numbers, how many random numbers
    do you need to generate distinct coupon number
"""
import random
class CouponNumber:
    def __init__(self, numberOfCoupon=0, count=0):
        self.numberOfCoupon=numberOfCoupon
        self.count=count
    def getCoupon(self):
        self.numberOfCoupon=int(input("Enter number of coupon:"))
        return self.numberOfCoupon
    def getRandomNum(self):
        for x in range(self.numberOfCoupon):
            randomNumber=random.randint(1, 100)
            count +=1
            size=randomNumber.__sizeof__()
        return count
obj=CouponNumber()
obj.getCoupon()
print(obj.getRandomNum())











