#syntax to define a function

def hello():         
    print('hello world')

hello()

#function with argument

def user(name):
    print("user name is ",name)

user('Amit')

#function with return statement

def user1(name):
    return name

user('Amit Boruah')

#function with multiple return statement

def user2():
    name='amit'
    email='amit@gmail.com'
    return name,email

name,email= user2()
print('name is',name)
print('email is',email)


def sum(a=10,b=20):
    print(a+b)

sum()               #calling without argument
sum(20,20)          #callling with argument

#non keyword argument

def add(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("sum",sum)

add(20,10,10)

#keyword  argument

def name1(**arg):
    for i,j in arg.items():
        print(i,j)

name1(firstname='Amit', lastname='Boruah')

#scope of variable

def func():
    x=20                                        #local variable
    print('value inside the function',x)        

x=10                                            #global variable
func()
print('value outside the function',x)


#import python file

import task4Demo            #import the function from task4demo.py to this file

task4Demo.hello()


#Arithmatic Operators

n1=10
n2=5

print('n1 + n2=',n1+n2)
print('n1 - n2=',n1-n2)
print('n1 / n2=',n1/n2)
print('n1 * n2=',n1*n2)
print('n1 % n2=',n1%n2)
print('n1 ** n2=',n1**n2)
print('n1 // n2=',n1//n2)


#comparison Operator

print('n1 < n2',n1<n2)
print('n1 > n2',n1>n2)
print('n1 <= n2',n1<=n2)
print('n1 >= n2',n1>=n2)
print('n1 != n2',n1!=n2)
print('n1 == n2',n1==n2)


#logical operator

n13a= 20                                    #other logical operators are 'and' , 'or', 'not'
n13b= 10
n13c= 30

if n13a<n13b and n13a<n13c:
 print(n13a,'is a smallest')

elif n13b<n13a and n13b<n13c:
 print(n13b,'is a smallest')

else:
 print(n13c,'is a smallest')


# Membership operator

n6=10                               #there are two membership perator 'in' and 'not in'
n7=15
l1=[5,10,20,25,30]

print(n6 in l1)
print(n7 in l1)

# identity operator

n8=20                           # two identity operator are 'is' and 'is not'
n9=20

print(n8 is n9)
print(n8 is not n9)

