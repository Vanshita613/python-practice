#factorial 

num=int(input("enter a number:"))
fact=1
i=1

while i<=num:
    fact=fact*i
    i+=1
print(fact)

#check prime number 
num=int(input("enter a number:"))

if num<=1:
    print(num,"is not a prime number!")
else:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
            print(num,"is a prime number!")


#fibonacci series
n=int(input("enter a number:"))

a=0
b=1

for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c