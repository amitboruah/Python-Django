print('hello world')                        # sign is use to create single line comment

a,b,c = 5,5.5,'five'                        # declaring 3 variable at a time and print them
print(a,'is integer value')
print('the valiue of b and c is',b,c)

name='Amit'                                 #Changing variable data
print(name)
name='Amit .B'
print(name)

d=e=10                                      #declaring same value in multiple varible
print('value of d and e',d,e)               

print(c,'is type of', type(c))              #type() is use to find the data type
print(b,'is float?', isinstance(5.5,float)) #isintance() check data type

fullName='Amit Boruah '
print(fullName)                             #it will print whole string
print(fullName[3])                          #it will print that index element
print(fullName[1:4])                        #it will in range
print(fullName[:3])                         #it will print 0 to that index
print(fullName*2)                           #it multiply the string
print(fullName+ 'hello')                    #it concatenate string

list1= [10,10.5,'amit',20]
print(list1[1])                             #it will print element in that index
print(list1[2:4])                           #it will give the range
list1[0]= 5                                 #change the value
print(list1)

tuple1= (20,30,'hello',10.5)                #commands are same as list
print(tuple1)                               #but we can not update tuple

dic= {1:10,2:'amit', 'key':20.5}             #dictonary
print(dic['key'])
print(dic[2])                                #calling element by its key

