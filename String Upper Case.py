class IOString:
    
    #constructor Method
    def __init__(self):
        self.str = " "
        
        
    def getString(self):
        self.str = input("Enter a String: ")
        
    def printString(self):
        print(f"Result is: {self.str.upper()}")
        
    
        
string1 = IOString()

#CALLING A METHOD
string1.getString()
string1.printString()

