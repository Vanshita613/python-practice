#Q2.check even or odd number

a=int(input("enter a nmber:"))

if a%2==0:
    print("number is even ")
else:
    print("number is odd!")




#Q3.Write a program to find the largest of three numbers.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a>b and a>c:
    print(a,"is the largest")
elif( b>a and b>c):
    print(b ,"is the largest")
else:
    print(c,"is the largest")



#Q4.Swap Two Numbers
#using temp variablwe
a=int(input("enter a number:"))
b=int(input("enter second number:"))
temp=a
a=b
b=temp

print("a=",a)
print("b=",b)


#without using temp variable
a=int(input("enter first number:"))
b=int(input("enter second number:"))

a,b=b,a

print("a=",a)
print("b=",b)


#Q5.