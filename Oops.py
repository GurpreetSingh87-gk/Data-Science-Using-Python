# Object Oriented Programming System(OOPS):-


# Oops:- Python is Oops language. Oops programming is done around an onject which is nothing but a
#        living or non-living real world entity. For example:- Person, Student, Car, Marker etc.

# ------------------

# Featurs of Oops:-

# Class:- Class is a user define data type. Class is a collection of similar objects.
# -----

# Object:- It is an instance of a class. Object is also called as class variable For example:-
# ------   If person is the class than Anderson, William etc. When object gets created memory will
#          be reserved for the class.

# Encapsulation:- The data members and methods of class both are wrap inside the class. That is the
# -------------   data is secured inside the class and to access the data we need to declare an
#                 object.

# Inheritance:- Even if the data is secured inside the class. It can be accessible in another class
# -----------   and it is called inheritance. For example:- Object of one class can inherit property
#               of another class.

# Polymorphism:- Poly means 'Many' Morphism means 'Forms'. For example:- Many forms of the some
# ------------   things.

# Abstraction:- The meaning is that sharing only the relevent data and not details.

# For Example:-
'''
class Student:
    def getData(Self):
        Self.rno = 1
        Self.name = "Sennery Wilton"

    def display(Self):
        print(Self.rno, Self.name)

S1=Student()
S1.getData()
S1.display()
'''
# =================================================================================================

# Class Methods with Parameters:-
# -----------------------------

# We can call the class methods by passing values which can be collected in parameters. These
# parameters should be declared inside the class definition after self parameters.


# For Example:-
'''
class Student:
    def getData(Self,r,n):
        Self.rno = r
        Self.name = n

    def display(Self):
        print(Self.rno, Self.name)

S1=Student()
S1.getData(1,"Denny")
S1.display()

S2=Student()
S2.getData(2,"Furgison")
S2.display()
'''
# =================================================================================================

# Q:- Write a program to display average of 2 subjects marks.
'''
# First Method:-

class Student:
    def getData(self,r,n,Subject1,Subject2):
        self.rno = r
        self.name = n
        self.Sub1 = Subject1
        self.Sub2 = Subject2
     
    def display(self):
        print(self.rno, self.name, self.avg)

    def getResult(self):
        self.avg = (self.Sub1 + self.Sub2)/ 2
   
print("RNo","Name","Marks")

S1=Student()
S1.getData(1,"Markus",65,89)

S2=Student()
S2.getData(2,"George",75,45)

S1.getResult()
S2.getResult()

S1.display()
S2.display()

# Second Method without getResult() call:-

class Student:
    def getData(self,r,n,Subject1,Subject2):
        self.rno = r
        self.name = n
        self.Sub1 = Subject1
        self.Sub2 = Subject2

    def display(self):
        avg = (self.Sub1 + self.Sub2)/ 2
        print(self.rno, self.name, avg)

print("RNo","Name","Marks")

S1=Student()
S1.getData(1,"Markus",65,89)

S2=Student()
S2.getData(2,"George",75,45)

S1.display()
S2.display()
'''
# =================================================================================================

# Contractors:-  Constructors is used to initialized data members of the class. It is the method
# -----------    of the class. It define by name --inti--(). Constructors gets called when object
#                of the class is created.

# There are 2 types of constructors:-

# 1. Default Constructor:- This constructor does not have any argument if we want to assign a
#    -------------------   common values to class element than use default constructor like all
#                          employee have common bonus amount.

# 2. Parameterized Constructor:- It is use if we want to assign different values for every object
#    -------------------------   of the class.

# =================================================================================================

# Inheritance:- It means object of one class can share methods and properties of another class.This
# -----------   can be done by inheriting a class for ex:- we can create parent-child relationship
#               between 2 clause.

# Types of Inheritance:-

# Single Level:- Parent ---> Child

# Multi Level:- Grandfather ---> Parent ---> Child

# Hierarchical Level:- Parent
#                        |
#              __________|_________
#             |          |         |
#          Child1      Child2   Child3

# Multiple Parent Class Single Base Class:- Parent1    Parent2   Parent3
#                                              |          |         |
#                                              |__________|_________|
#                                                         |
#                                                       Child

# =================================================================================================

# Single Level Inheritance:-

# It has one parent class and one child class. Child class object can access properties of Parent
# class. Parent class is also called base class and Child class is derived class.

# For Example:-
'''
class Parent:
    def input(self):
        print("Parent Class Fun Called")

class Child(Parent):
    def getinfo(self):
        print("Input Fun Called")

C1=Child()
C1.input()
C1.getinfo()

# Q:- Create a class Student as parent class with data members roll no, name and inherit it in the
#     child class.

class Parent:
    def getData(self,r,n):
        self.rno = r
        self.name = n

class child(Parent):
    def display(self):
        print(self.rno, self.name)

C1=child()
C1.getData(1,"ABC")
C1.display()
'''
# =================================================================================================

# Multiple Inheritance:- In this there are multiple parent and single child class. Parent class can
# --------------------   be inherited by the class name separated by comma.

# For Example:-

class Student:
    def getData(self,r,n):
        self.rno = r
        self.name = n

class Exam:
    def getMarks(self, m1, m2):
        self.sub1 = m1
        self.sub2 = m2

class Result(Student, Exam):
    def getResult(self):
        print(self.rno, self.name)
        self.avgmarks =(self.sub1 + self.sub2)/2
        print("Average Marks:",self.avgmarks)

R1=Result()
R1.getData(1,"Perry")
R1.getMarks(25,35)
R1.getResult()

