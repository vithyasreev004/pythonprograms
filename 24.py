class Area:
    def circle(self):
        self.r = float(input("ENTER THE RADIUS OF THE CIRCLE:"))
    def square(self):
        self.a = float(input("ENTER THE SIDE OF THE CIRCLE:"))
    def rectangle(self):
        self.l = float(input("ENTER THE LENGTH OF THE CIRCLE:"))
        self.b = float(input("ENTER THE BREADTH OF THE CIRCLE:"))
    def triangle(self):
        self.h = float(input("ENTER THE HEIGHT OF THE CIRCLE:"))
        self.b = float(input("ENTER THE BREADTH OF THE CIRCLE:"))

class MyClass(Area):
    def acircle(self):
        self.circle()  
        pi = 3.17  
        area = pi * self.r ** 2  
        print("THE AREA OF THE CIRCLE IS:", area)
    def asquare(self):
        self.square()  
        sarea =self.a*self.a  
        print("THE AREA OF THE CIRCLE IS:",sarea)
    def arectangle(self):
        self.rectangle()  
        rarea =self.l*self.b  
        print("THE AREA OF THE CIRCLE IS:",rarea)
    def atriangle(self):
        self.triangle()  
        tarea =0.5*self.b*self.h  
        print("THE AREA OF THE CIRCLE IS:",tarea)

obj1 = MyClass()
obj1.acircle()
obj1.asquare()
obj1.arectangle()
obj1.atriangle()
