#Q1

a=("Python is a case sensitive language")
print(len(a))
print(a[::-1])
b=slice(10,26)
print(a[b])
c=a.replace("a case sensitive", "object oriented")
print(c)
d=a.index('a')
print(d)
e=a.replace(' ','')
print(e)

#Q2

Name=input("Enter your name =")
SID =input("Enter your sid =")
Department=input("Enter your department=")
CGPA = float(input("Enter your cgpa ="))
print("\nHey, "+Name+" Here!")
print("My SID is "+ str(SID))
print("I am from "+Department+" and my CGPA is "+str(CGPA))

#Q3

a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a,b << 2)
print(a>>2, b>>4)

#Q4

Num1 =int(input("Number 1"))
Num2 =int(input("Number 2"))
Num3 =int(input("Number 3"))

if (Num1>Num2) and (Num1>Num3):
    largest = "Number 1"
    #print("num1 is the largest")
elif (Num2>Num1) and (Num2> Num3):
    largest = "Number 2"
    #print("num2 is the largest")
else:
    largest = "Number 3"
    #print("num3 is the largest")

print("The largest number is "+largest)

#Q5

a=input("Write a sentence ")
b=a.find('name')

if b==-1:
    print('No')

else:
    print('Yes')

#Q6

a=float(input('Write the first number '))
b=float(input('Write the second number '))
c=float(input('Write the third number '))

a=int(a)
b=int(b)
c=int(c)

print(type(a))
if (a<b+c) and (b<a+c) and (c<a+b):
    print('Yes')

else: 
    print('No')