class rect():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rect: "))
b=int(input("Enter breadth of rect: "))
obj=rectangle(a,b)
print("Area of rect:",obj.area())
 
print()
