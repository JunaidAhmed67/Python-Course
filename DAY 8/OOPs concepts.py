# # inheritence taking properties from mother class 
# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stoped...")

# class toyota_car(Car):

#     def __init__(self,name):
#         self.name = name
    
# class Fortuner(toyota_car):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("petrol")
# car1.start()
# print(car1.type)



       
# class A:
#     varA= "welcome to class A"
# class B:
#     varB= "welcome to class B"
# class C(A,B):
#     varC= "welcome to class C"

# user1 = C()
# print(C.varA)
# print(C.varB)
# print(C.varC)

# class Car:
#     def __init__(self,type):
#      self.type = type
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stoped...")

# class toyota_car(Car):

#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name

# car1 = toyota_car("mona","electric")
# print(car1.name)
# print(car1.type)
# class Car:
#     car_name ="lolo"
#     def __init__(self,type):
#      self.type = type
    

#     @classmethod
#     def cng_car_name(cls):
#        cls.car_name = "bobo"

#     @property
#     def start():
#       return 89



# car1 =Car("mona")
# print(car1.car_name)
# car1.cng_car_name()
# print(car1.car_name)
# print(car1.start)

# class Rectangle:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def area(self):
#         return self.width * self.height

# r = Rectangle(10, 5)

# print(r.area)

# class Complex_Number():
#     def __init__(self,real ,img):
#         self.real = real
#         self.img = img

#     def showNumbers(self):
#         print(self.real,"i ",self.img,"j")

#     def __add__(self,obj2):
#         newReal = self.real + obj2.real
#         newImg = self.img + obj2.img
#         return Complex_Number(newReal,newImg)
#     def __sub__(self,obj2):
        
#         newReal = self.real - obj2.real
#         newImg = self.img - obj2.img
#         return Complex_Number(newReal,newImg)

# obj1 = Complex_Number(2, 8)
# obj1.showNumbers()
# obj2 = Complex_Number(3, 1)
# obj2.showNumbers()

# obj3 = obj1 + obj2
# obj3.showNumbers()


# obj4 = obj1 - obj2
# obj4.showNumbers()


# class Circle():
#     pi = 3.142
#     def __init__(self,radius):
#         self.radius =radius
#         self.pi = (22/7)

#     def area(self):
#         return self.pi*self.radius*self.radius
    
    
#     def perimeter(self):
#         return 2*self.pi*self.radius
    

# cir1 = Circle(21)
# print(cir1.area())
# print(cir1.perimeter())

# class Employee():
#     def __init__(self,role ,dep ,sel):
#         self.role = role
#         self.dep = dep 
#         self.sel = sel

#     def showDetails(self):
#         print("Employe role: ",self.role)
#         print("Employe department: ",self.dep)
#         print("Employe selary: ",self.sel)

# class Engineer(Employee):
#     def __init__(self, name , age ):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","780000")





# eng1 = Engineer("junaid",22) 
# eng1.showDetails()


class Order():
    def __init__(self, item , price):
        self.item = item 
        self.price = price
    
    def __gt__(self,ord2):
        if(self.price>ord2.price):
            print("True")
        else:
            print("False")
             
        
ord1 = Order("book",200)
ord2 = Order("glass", 1000)
ord3 = ord1>ord2
