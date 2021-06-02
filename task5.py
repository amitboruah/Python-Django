# 1. Create a class cal1 that will calculate sum of three numbers. Create
# setdata() method which has three parameters that contain numbers.
# Create display() method that will calculate sum and display sum.

class cal1():
    n1=''
    n2=''
    n3=''

    def setdata(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3

    def display(self):
        sum=self.n1+self.n2+self.n3
        print('the sum of three number is',sum)

c=cal1()
c.setdata(10,20,30)
c.display()



# 2. Create a class cal2 that will calculate area of a circle. Create setdata()
# method that should take radius from the user. Create area() method
# that will calculate area . Create display() method that will display area .


class cal2():
    raius=''
    a=''

    def setdata1(self):
        radius= int(input('Enter the radius :'))
        self.radius=radius

    def area(self):
        self.a=3.14*(self.radius*self.radius)

    def display1(self):
        print('Area of the cirle is ',self.a)

c2=cal2()
c2.setdata1()
c2.area()
c2.display1()



# 3. Create a class cal3 that will calculate simple interest. Create
# constructor method which has three parameters .Create calInterest()
# method that will calculate Interest . Create display() method that will
# display Interest

class cal3():
    p =''
    r =''
    t =''
    a =''

    def __init__(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t

    def calInterest(self):
        self.a = self.p * (1 + self.r * self.t )
    
    def display3(self):
        print("The Simple Intrest is :",self.a)

c3=cal3(10,2,2)
c3.calInterest()
c3.display3()


# 4. Create a class cal4 that will calculate square of a number. Create
# setdata() method which has one parameters that contain number.
# Create display() method that will calculate sum.(Function should
# return value)


class cal4():
    n4=''
    sq=''

    def setdata4(self,num):
        self.n4=num
    
    def display4(self):
        self.sq = self.n4 * self.n4
        print('Square of a number is :',self.sq)

c4=cal4()
c4.setdata4(5)
c4.display4()



# 5. Consider an employee class, which contains fields such as name and
# designation. And a subclass, which contains a field salary. Write a
# program for inheriting this relation


class employee():
    
    def emName(self):
        print('Employee name :')
        print('Employee designation :')

class empl(employee):

    def salary(self):
        print('Employee salary :')

e5=empl()
e5.emName()
e5.salary()



# 6. Create a class cal5 that will calculate area of a rectangle. Create
# constructor method which has two parameters .Create calArea()
# method that will calculate area of a rectangle. Create display() method
# that will display area of a rectangle.


class cal5():
    l=''
    w=''
    a=''

    def __init__(self,length,width):
        self.l=length
        self.w=width
    
    def calArea(self):
        self.a = self.l * self.w

    def display6(self):
        print('The area of Rectangle is :',self.a)

c6= cal5(4,2)
c6.calArea()
c6.display6()



# 7. Create a class cal6 that will calculate area of a square. Create setdata()
# method that should take length from the user. Create area() method
# that will calculate area . Create display() method that will display area .


class cal6():
    length=''
    area=''


    def setdata7(self):
        self.length= int(input("Enter the length :"))

    def area7(self):
        self.area = self.length * self.length
    
    def display7(self):
        print('The are of a Square is :', self.area)

c7= cal6()
c7.setdata7()
c7.area7()
c7.display7()



# 8. Write a program with use of inheritance: Define a class publisher that
# stores the name of the title. Derive two classes book and tape, which
# inherit publisher. Book class contains member data called page no and
# tape class contain time for playing. Define functions in the appropriate
# classes to get and print the details.

class publisher():
    t=''

    def title(self):
        self.t= input('Enter the name of the Title :')

class book(publisher):
    pnum=''

    def page(self):
        self.pnum= int(input('Enter the page number :'))

    def disp8(self):
        print('The title name is :',self.t)
        print('The page number is :',self.pnum)

class tape(publisher):
    time=''
    def timep(self):
        self.time= int(input('Enter time for playing :'))

    def disp8(self):
        print('The time for playing is :',self.time)


c8a=book()
c8a.title()
c8a.page()
c8b=tape()
c8b.timep()
c8a.disp8()
c8b.disp8()



# 9. Create a class called scheme with scheme_id,
# scheme_name,outgoing_rate, and message_charge. Derive customer
# class form scheme and include cust_id, name and mobile_no
# data.Define necessary functions to read and display data.

class scheme():
    scheme_id=204
    scheme_name='unlimited call'
    outgoing_rate=599
    message_charge=1

class customer(scheme):
    cust_id='Amit01'
    name='Amit Boruah'
    mobile_no=1234567890

    def detail(self):
        print('customer name :',self.name)
        print('customer id :',self.cust_id)
        print('customer mobile number :',self.mobile_no)
        print('scheme id :',self.scheme_id)
        print('scheme name :',self.scheme_name)
        print('scheme outgoing rate :',self.outgoing_rate)
        print('scheme message rate :',self.message_charge)
      
c9=customer()
c9.detail()



# 10.Create a arith class. The class should have a parameterized constructor
# and methods to add, subtract and multiply two numbers and to return
# the answers.

class arith():
    n1=''
    n2=''

    def __init__(self,num1,num2):
        self.n1=num1
        self.n2=num2

    def cal10(self):
        add= self.n1 + self.n2
        sub= self.n1 - self.n2
        multi=self.n1 * self.n2

        print('addition is :',add)
        print('subtraction is :',sub)
        print('multiplication is :',multi)
        
c10=arith(10,5)
c10.cal10()