from dataclasses import dataclass

@dataclass
class Rectangle:
    height: int
    width: int  
    
        
    def getPeremiter(self):
        peremiter = self.height * 2 + self.width * 2
        return peremiter
    
    def getArea(self):
        area = self.height * self.width
        return area
    
    def getPrint(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.height - 2):
            s += "* "
            s += "  " * (self.width - 2)
            s += "* \n"
        s += w
        return  s
    
def main():
    print(" Rectangle Calculator")
    print()
    
    again = "y"
    while again.lower() == "y":
        height  = int(input("Height:    "))
        width = int(input("Width:   "))
    
        rectangle = Rectangle(height, width)
        print("Perimter:", rectangle.getPeremiter())
        print("Area:", rectangle.getArea())
        print(rectangle.getPrint())
        
        again = input("Continue? (y/n): ")
    print("Bye!")
    
if __name__ == "__main__":
    main()
        
    


