"""
   * author - Akshay Tekam
   * date - 10/01/2021
   * time - 04:55:43
   * package - ${PACKAGE_NAME}
   * Title - Determine if it is a Leap Year
"""
class LeapYear:
    # Determine a four digit year
    # by checking with 400, 4 and 100.
    def determinYear(self):
        year = int(input("Enter a year: "))
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print("Leap Year")
        else:
            print("Not Leap Year")
obj=LeapYear()
obj.determinYear()