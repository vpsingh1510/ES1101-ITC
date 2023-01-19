#calculate the grades of students
a=int(input("enter your marks"))
if a<25:
   print("F")
elif 25<=a<45:
   print("E")
elif 45<=a<50:
   print("D")
elif 50<=a<60:
   print("C")
elif 60<=a<80:
   print("B")
else:
   print("A")
#CHECK WHETHER THE YEAR IS LAP YEAR OR NOT
Y=int(input("enter any year"))
if Y%4==0 and Y%100==0:
    print("not a leap year")
elif Y%100==0 and Y%400==0 :
    print("a leap year")
elif Y%4==0:
    print("a leap year")
else:
    print("not a leap year")
import random
print("QUESTION 1-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M, "X", N)
a=int(input("your answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 2-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 3-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 4-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 5-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 6-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 7-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 8-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 9-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
print("QUESTION 10-")
M=random.randint(1, 20)
N=random.randint(1, 20)
print(M,"X",N)
a=int(input("answer="))
if a==M*N:
    print("right")
else:
    print("wrong")
#determine the no. of pieces present in bowl
for candies in range(200):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue

    print(str(candies) + " is the answer!")