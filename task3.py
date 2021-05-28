#1.Program to Calculate the average of five number

num1= int(input('Enter the first number :'))
num2= int(input('Enter the second number :'))
num3= int(input('Enter the third number :'))
num4= int(input('Enter the fourth number :'))
num5= int(input('Enter the fifth number :'))

avg= (num1+num2+num3+num4+num5)/5

print('The Average of five number is :',avg)


#2.	Check whether number is even or odd.

num= int(input('Enter the number :'))

if num % 2 == 0:
    print(num,'is Even number')

else :
    print(num,'is Odd number')    


#3.	Take a year and check whether it is leap year or not

year= int(input('Enter the year :'))

if year % 4 == 0:
        print(year,'is a leap year')
    
else :
    print(year,'is not a leap year')

    
#4.	Take a number and check whether it is zero, positive or negative.

numCheck= int(input('Enter the number :'))

if numCheck > 0:
     print(numCheck,'is greater than zero')   
   

elif numCheck == 0:
    print(numCheck,'is equal to zero')

else:
    print(numCheck,'is less than zero')  



#5.	Take 2 numbers and display greatest number. (Also check equal number condition)

n1= int(input('Enter the first number :'))
n2= int(input('Enter the second number :'))

if n1>n2:
    print(n1,'is greater than ',n2)

elif n1==n2:
    print(n1, 'is equal to ',n2)

else:
    print(n1,'is less than ',n2)          


#6.	Take a number and find factorial of that number.      

numfact= int(input('Enter the value :'))
fact=1
for i in range (1,numfact+1,1)  :
    
    fact=fact*i
print('Factorial is ',fact) 


#7.	Write a program to swap 2 numbers using third variable.

n7a= int(input('Enter the first Number :'))
n7b= int(input('Enter the seconf number :'))

print('value before swapping :-')
print('first number :',n7a)
print('second number :',n7b) 

temp = n7a
n7a = n7b
n7b = temp

print('value after swapping :-')
print('first number :',n7a)
print('second number :',n7b)


#8.	Take 2 numbers and find smallest number.

n8a=int(input('Enter the first number :'))
n8b=int(input('Enter the second number :'))

if n8a<n8b:
    print(n8a,'is smallest number')

else :
    print(n8b,'is smallest number')


#9.	Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.

ncheck=int(input('Enter the number :'))

if ncheck<100 :
    print(ncheck,'is less than 100')
    if ncheck % 2 ==0:
        print(ncheck,'is a Even number')
    else:
        print(ncheck,'is a Odd number')    

else:
    print(ncheck,'is not less than 100')



#10.	Take a number to print the square of a number if it is less than 10.

sqNum= int(input('Enter the number :'))

if sqNum<10:
    sq=sqNum*sqNum
    print('The square of a number is :',sq)

else:
    print(sqNum,'is not less than 10')   



#11.	Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .

numCheck1= int(input('Enter the number :'))

if numCheck1 >= 0:
    if numCheck1 == 0:
        print(numCheck1,'is equal to zero')

    else:
        print(numCheck1,'is greater than zero')

else:
    print(numCheck1,'is less than zero')



#12.	Take 3 numbers and find greatest number using nested IF….ELSE statement. 

n12a=int(input('Enter the first Number :'))
n12b=int(input('Enter the second Number :'))
n12c=int(input('Enter the third Number :'))

if n12a>n12b:
    if n12a>n12c:
        print(n12a,'is the Greatest number')
    
    else:
        print(n12c,'is the Greatest number')

else:
    print(n12b,'is the Greatest number')



#13.	Take 3 numbers and find smallest number using logical operator.

n13a= int(input('Enter the first number :'))
n13b= int(input('Enter the second number :'))
n13c= int(input('Enter the third number :'))

if n13a<n13b and n13a<n13c:
 print(n13a,'is a smallest')

elif n13b<n13a and n13b<n13c:
 print(n13b,'is a smallest')

else:
 print(n13c,'is a smallest')    


#14.	Write a program to swap 2 numbers without taking third variable.

n14a= int(input('Enter the first number :'))
n14b= int(input('Enter the second number :'))

print('value before swapping :-')
print('first number :',n14a)
print('second number :',n14b) 

n14a,n14b=n14b,n14a

print('value after swapping :-')
print('first number :',n14a)
print('second number :',n14b)

    

#15.	Take starting number and ending number from the user and print following series

n15a= int(input('Enter the starting number :'))
n15b= int(input('Enter the ending number (less than first number) :'))

for i in range(n15a,n15b-1,-3):
 print(i)