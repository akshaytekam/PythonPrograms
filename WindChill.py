"""
   * author - Akshay Tekam
   * date - 11/01/2021
   * time - 22:44:36
   * package - ${PACKAGE_NAME}
   * Title - Calculate wind chill factor for a temperature
"""
import math
class WindChill:
    # By taking the values of t and v
    # putting them into factor equation
    def findFactor(self):
        v = float(input("Input wind speed: "))
        t = float(input("Input temperature in Fahrenheit: "))
        w = 35.74 + (0.6215*t) - 35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16)  # equation for Fahrenheit
        print(w)
obj=WindChill()
obj.findFactor()


