"""
   * author - Akshay Tekam
   * date - 11/01/2021
   * time - 08:76:56
   * package - ${PACKAGE_NAME}
   * Title -  Read in N integers and counts the
       number of triples that sum to exactly 0
"""
class SumOfTriplet:
    # identify the triplets and sum them together
    # to get zero value.
    def findTriplets(self,arr, n):
        found = True
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):

                    if (arr[i] + arr[j] + arr[k] == 0):
                        print(arr[i], arr[j], arr[k])
                        found = True

arr = [0, -1, 2, -3, 1]          # take it from array
n = len(arr)
obj=SumOfTriplet()
obj.findTriplets(arr, n)

