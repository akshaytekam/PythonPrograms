"""
   * author - Akshay Tekam
   * date - 10/01/2021
   * time - 06:45:66
   * package - ${PACKAGE_NAME}
   * Title - User Input and Replace String Template
"""
class String:
    def replace(self):
        name = input("Enter your name: ")
        txt = "Hello " + name + " how are you?"
        print(txt)
        x = txt.replace(name, "Akshay")
        print(x)
obj=String()
obj.replace()
