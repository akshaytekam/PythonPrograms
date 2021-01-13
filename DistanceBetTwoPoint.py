"""
   * author - Akshay Tekam
   * date - ${DATE}
   * time - ${TIME}
   * package - ${PACKAGE_NAME}
   * Title - prints the Euclidean distance from the
           point(x,y)to the origin(0,0).
"""
import math
class Distance:
    # calculate distance between two points
    def findDistance(self):

        p1 = [4, 2]
        p2 = [0, 0]

        # Formula for Euclidean distance
        distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
        print(distance)
obj=Distance()
obj.findDistance()
