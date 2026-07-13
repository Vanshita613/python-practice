# str="vanshita"
# print(str.endswith("vv"))

# str="my name is sia"
# print(str.find("sia"))

# str= " hi hi hello"
# print(str.count("hi"))

# name  = input("enter your first name:")
# len = len( name)
# print (  len, name  )

# marks = 74
# if(marks >=90):
#      grade ="A"
# elif(marks >=80 and marks < 90):
#     grade = "B"
# elif(marks >=70 and marks < 80):
#      grade = "C"

# elif (marks >= 60 and marks <70):
#      grade = "D"

# print ("grade of the student", grade)  #output: grade of the student is c 


# a=int (input("enter a number"))
# b = int(input( "enter a number"))
# c = int(input( "enter a number"))

# if ( a>=b and a>=c):
#     print( "first number is the largest", a)

# elif(b>=c):
#     print ( "second number is the largest ", b)

# else:
#     print( "third number is the largest")

# a= int(input (" enter number: "))
# if(a% 7==0) :
#     print ("multiple of 7")
# else:
#     print ("not a multiple")


# mov1 = input("enter a movie")
# mov2 = input("enter a movie")
# mov3 = input("enter a movie")

# list=[ mov1 , mov2 , mov3]
# print ( list)

# info = {
#     "name":  "jimin",
#     "age"  : "30",
#     "city" :"seoul",
# }

# print ( info)

# dict = {
#     "word" :"happy",
#     "means" : "happii",
# }

# dict.update ({"opposite":"sad"})
# print (dict)


# set ={ "park jimin"}

# print ( type (set))


# count = 1
# while count <=8:
#     print ("sia")
#     count += 1
#     print(count)

# set1= {5, 6,6 ,7}
# set2= {5 , 9,5,4 ,0}

# print(set1.union(set2))

# dict ={
#     "table" : ["a piece of furniture","list of facts and figures"],
#  "cat" : "a small animal" 

#     }
# print ( dict)


# marks = {}

# x = int (input("enter eng : "))
# marks.update({"eng":x})

# x =int(input("enter hindi :"))
# marks.update({ "hindi" : x})

# x= int(input("enter maths : "))
# marks.update({"maths": x})

# print(marks)

# count= 1
# while count<=4:
#     print ("hoseok")
#     count += 1

# count = 1
# while count <=100:
#     print ( count)
#     count +=1


# i=100
# while i >=1:
#     print (i)
#     i -=1

# n=int(input("enter a number"))
# i=1
# while i<=10:
#     print(n*i)
#     i +=1
  
# index = 0
# nums=[1 , 4 ,9 ,16, 25,36,49,64,81,100]
# while index < len(nums):
#     print( nums[index])
#     index +=1
    
# nums=[1,2,3,5,6]

# for val in nums:
#     print(val)

# names = [ "jim", "v" ,"kook","rm" ,"hope" ,"suga" ,"jin"]
# for el in names:
#     print ( el)

# nums=[ 1,4,9,16,24,36,49,64,81,100]

# for el in nums:
#     print(el)

# nums =( 1,4,9,16,24,36,49,64,81,100)
# x = 49
# for el in nums :
#     if (el==x):
#      print ( x)

# for i in range(17):
#     print (i)

# for i in range(1 , 101):

#     print (i)

# for i in range(100,0 , -1):
#     print (i)

# n = int(input("enter a number"))

# for i in range( 1,11):
#     print ( n*i)

# n = int ( input ("enter a number: "))
# i = 1
# while i <= n:
#     print ( i + n)
#     i +=1

# def calc_sum(a,b):
#     return a+b
# i = calc_sum ( 7,7)
# print (i)

# def calc_sub(a,b):
#     return a-b
# v= calc_sub (999,89)
# print (v)

# def multiply(a,b,c):
#     return a*b*c
# j= multiply (8,67,4)
# print(j)

# def calc_avg(a,b,c):
#     sum= a+b+c
#     avg= sum/3

#     print (avg)
#     return avg
# calc_avg(1,4,2)

# def calc_avg (a,b,c):
#     sum= a+b+c
#     avg= sum/3
 
#     print ( avg )
   
# calc_avg (6,7,8)


# cities =["seoul","tokyo","indore","jimin", "suga", "jungkoook"]
  
# def city_nm( list):
#      print (len(list))

# city_nm(cities)

#

# def idol_nm(list):
#      print(len(list))

# idol_nm(names)

# list=["vansh","riki", "sam"]
# print(list[0] , end=" ")
# print(list[2] , end=" ")

# def calc_fact(n):
#     fact=1
#

# n=int(input("enter a number:"))

# if ( n %2 !=0):
#     print("Weird")
# if (n%2==0 and 2<= n<=5):
#     print("Not Weird")
# if (n%2==0 and 6<=n<=20):
#     print("Weird")
# if ( n%2==0 and n>20):
#     print("Not Weird")


# name="siddarth"
# print(name[4])


# str="vanshita"
# len=len(str)
# print(len)

# word= "PYTHON"
# print(word[0:5])

# name="apple"
# print(name[-3:-1])


#find the largest number among three numbers
# num_1=int(input("enter first number:"))
# num_2=int(input("enter second number:"))
# num_3=int(input("enter third number:"))

# if (num_1 > num_2 and num_1> num_3):
#     print(num_1, "is the largest")
# elif (num_2 >num_1 and num_2 > num_3):
#     print(num_2 , "is the largest")
# else :
#     print(num_3 ,"is the largest")


# n=65
# if(n<98):
#     print("n is less than 98")


# Given a number, check if it is divisible by 9. If yes, check if it is even or odd.

# num=int(input("enter a number:"))

# if (num%9==0) :
#     if (num%2==0):
#         print("number is divisible by 9 and number is even!") 
        
#     else:
#         print("number is divisible by 9 and numner is odd!")
        
# else: 
#     print("the number is not divisible by 9!")



# check wether given number is positiv , negative or zero
# num=int(input("enter a number:"))
    
# if( num>0):
#         print("number is positive")
        
# elif(num<0):
#     print("number is negative")
# else :
#     print("number is zero")


# # LEAP YEAR CHECKER
# year=int(input("enter the year:"))

# if(year % 400==0) or( year % 4==0 and year % 100!=0):
#         print("Leap year!")
# else:
#     print("not a leap year!")
    
    


#  marks=int(input("enter the marks:"))

# if (marks>=90):
#     print("GRADE A")
# elif( marks>=80):
#     print("GRADE B")
# elif(marks>=70):
#     print("GRADE C")
# elif(marks>=60):
#     print("GRADE D")
# else:
#     print("FAIL!")
    

# n = 10
# i =1
# sum = 0
# while(i<=n):
#    sum+=i
#    i+=1
# print(sum)



# i=1
# while(i<=10):
#  print(i)
#  i+=1

# n=int(input("enter a nubmer:"))
# i=1
# while(i<=10):
#     print(i*n)
#     i+=1

# i=100
# while(i<=1):
#     print(i)
#     i-=1

# n = int(input("Enter a number: "))

# fact = 1
# i = 1

# while i <= n:
#     fact = fact * i
#     i = i + 1``

# print("Factorial =", fact)


# i=1
# while(i<=5):
#     print(i**2)
#     i+=1
    

        
# i=1
# while(i<=10):
#     print(i**3)
#     i+=1

# i=1
# while(i<=10):
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

      
# num=(3,5,6,6,2,5,3,)
# for el in num:
#     print(el)


num=(1,4,9,16,25,36,49,64,81,100)
x=64

idx=0
for el in num:
    if(el==x):
        print("found at index",idx)
      
    idx += 1

for i in range(2,21,2):
    print(i)


for i in range(1,11):
    print(i)