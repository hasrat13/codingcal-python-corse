class square:
    def __init__(self,side):
        self.side=side
    def area(self):
            print("my area is :",self.side**2)
class circle:
    def __init__(self,radius):
          self.radius=radius
    def area(self):
         print("my area is :", 3.14*self.radius*self.radius)
osquare=square(5)
ocircle=circle(5)
for shape in(ocircle,osquare):
    shape.area()