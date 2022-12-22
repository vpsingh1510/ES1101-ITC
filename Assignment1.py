# Assignment 1
# Q1

a=int(input("First"))
b=int(input("Second"))
c=int(input("Third"))

d=(a+b+c)/3
print(d)

#Q2

a=int(input("What is your gross income?"))
b=int(input("No. of dependants"))

c=a-10000-3000*b
d=c*0.2
print(d)

#Q3

a=int(input("No. of seconds"))
b=a//60
c=a%60
Minutes = print(b)
Seconds = print(c)

#Q4

a = "25"
b= 25
c=25.0
d=int(a) + b+int(c)
e=str(d)
print(e)
print(type(e))

#Q5

import math
i=0
for i in range(0,345,15):
#x=math.pi/i

    a=math.cos(math.radians(i))
    b=math.sin(math.radians(i))
    print(round(a,4), round(b,4))
