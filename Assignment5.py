#Q1
string=input("Enter a String ")
print(string[::-1])
#Q2
lower_range=int(input("Enter a lower range"))
higher_range=int(input("Enter a Upper range"))
num1=int(input("number divided by"))
i=lower_range
while i in range (lower_range,higher_range):
    if i%num1==0:
        print(i)
        i+=1
    else:
        i+=1
#Q3
a=int(input('Write the first number '))
b=int(input('Write the second number '))
c=int(input('Write the third number '))

s=(a+b+c)/2
area_a= s*(s-a)*(s-b)*(s-c)
area=area_a**0.5
if (a<b+c) and (b<a+c) and (c<a+b):
    print('Yes the triangle is posible and has an area of', area)
else: 
    print('No')
#Q4
i=1
while i<5:
    print("* "*i)
    i+=1
while i>0:
    print("* "*i)
    i-=1
#Q5
rows = int(input("Enter Rows = "))
alphabet = 65
i = 0

while(i < rows):
    j = 0
    while(j <= i):
        if alphabet==91:
            alphabet=65
    
        print(chr(alphabet), end = ' ')
        alphabet = alphabet + 1
        j = j + 1
    print()
    i = i + 1
#Q6
lower=int(input("Enter lower limit"))
upper=int(input("Enter your limit"))

for x in range(lower,upper+1):
    if x>1:
        for i in range(2,x):
            if x%i==0:
                break
        
        else:
            print(x)
#Q7
i=0
while i<500:
    if i%7==0 and i%11==0:
        print(i)
        i+=1
            
    else:
            i+=1
#Q8
a=(input("Enter 10 integers :").split(" "))
positve=[]
negative=[]
odd=[]
even=[]
for i in a:
    i=int(i)
    if i>0:
        positve.append(i)
print("Positive integers in input is ",positve)
for i in a:
    i=int(i)
    if i<0:
        negative.append(i)
print("Negative integers in input is ",negative)
for i in a:
    i=int(i)
    if i%2!=0:
        odd.append(i)
print("odd integers in input is ",odd)
for i in a:
    i=int(i)
    if i%2==0:
        even.append(i)
print("Even integers in input is ",even)
dic1={}
for i in a:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
for i in dic1:
    print("Number of times",i,"in input is", dic1.get(i))
#Q9
a=(input("Enter Sentence :").split(" "))
dic1={}
for i in a:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
    
for i in dic1:
    print("Number of times",i,"in input is", dic1.get(i))