#a,b=map(int,input("Enter two numbers : ").split()[:2])
#print(f"first number: {a}, second number: {b}")


#operation=int(input("enter a number of following operation that you want to perform"))

#if operation==1  or operation==2 or operation==3 or operation==4



#has_id=input("Enter if he has id (Yes/No) : ").split().lower() 
#if has_id=="No":
    #print("piease bring your id!!")
#elif has_id=="Yes":
   #print("welcome")
#else:
 #   print("Enter a valid value")    



#number=int(input("enter a number"))
#for i in range (1,number+2):
 #   if i%2==0:
  #  print(f"{i} is even")
    # print(f"{i} is sum")

# str=input("enter a string :").strip().lower()
# str2=""
# length=len(str)
# for element in range(length-1,-1,-1):
#    str2=str2+str[element]
# if str==str2:
#    print("string is palindrom")
# else:
#    print("string is not palindrom")

# word = "Python"

# count = 0

# for character in word:
#     count = count + 1

# print("Characters:", count)

# for i in range(3):
#     for j in range(2):
#         print(i, j)

# for row in range(3):
#     for column in range(4):
#         print("*",end=" ")
#     print()


# int("hello")
# text = 'DataScience'
# print(text[2:8:2])

# for i in range(1,6):
#     print("*",end="")

# for i in range (5):
#     for k in range(5):
#       print("*", end="")
#     print()


# for i in range (4,1,-1):
#     for i in range (i):
#         print("*", end="")
#     print()


# number=int(input("enter a number:"))
# for i in range(1,number):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# num=int (input("enter a number:"))
# for i in range (num,0,-1):
#     for j in range(num+1,-1,-1):
#         print(" ",end="")
#     for k in range (1,+num+1):
#         print("*",end="")
#     print()


# for i in range(1,6):
#     for j in range (1,6-1):
#         print(" ",end="")
#     for k in range (1,2*i-1):
#         print("*",end="")
#     print("")



# for i in range(5 ):
#     for j in range(5 ):
#         if i==5-1 or j==0 or j==5-1: 
#            print("*", end="")
#         else:
#          print(" ", end="")
#     print()




# i = 2

# while i <= 10:
#     print(i)
#     i = i + 2

# i=10
# while  i >=1:
#     print(i)
#     i-=1


# i = 20
# while i >=2:
#     print(i)
#     i-=2


# number=int(input("enter a number:"))
# while number!=0:
#     print("your number",number)
#     number=int(input("enter your number:"))
# print("loop ended")                


# number=int(input("enter a number:"))
# total=0
# while number!=0:
#     total=total+number
#     number=int(input("enter a number:"))
# print("sum",total)


# str = input("enter a character :")
# flag=True
# i=0
# j=len(str)-1
# while i<j:
#     if str[i]!=str[i]:
#         flag = False
#     i+=1
#     j-=1
# if flag:
#     print("chacter is palindrome")
# else:
#     print("chacter is not palindrome")



# str1=input("enter a string:")
# i=0
# j=len(str1)-1
# flag=True
# while(i<j):
#     if str1[i]==str1[j]:
#         i+=1
#         j-=1
#     else:
#         flag=False
#         i=j
# if flag:
#     print("given string is palidrome!!")
# else:
#     print("given string is not palidrome!!")



# number=2345
# while number>0:
#     digit = number % 10
#     print(digit)
#     number = number//10



# number = int(input("enter a number:"))
# total= 0

# while number > 0:
#     digit = number % 10
#     total = total + digit
#     number = number // 10
# print("sum",total)


# number = 121
# original_number = number
# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10

# if original_number == reverse:
#     print(f"{original_number} is a palindrome!")
# else:
#     print(f"{original_number} is not a palindrome.")

# number = int(input("Enter a number: "))

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10

# print("Reverse:", reverse)


# i = 10

# while i > 0:
#     print(i)
#     i = i - 1


# row = 1

# while row <= 2:
#     column = 1

#     while column <= 3:
#         print("*", end="")
#         column = column + 1

#     print()
#     row = row + 1


# row = 1
# column = 1

# while row <= 3:

#     while column <= 4:
#         print("*", end="")
#         column = column + 1

#     print()
#     row = row + 1


# color = "red"

# match color:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _:
#         print("Invalid Color")

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# choice = int(input("Enter your choice (1-4): "))

# match choice:
#     case 1:
#         print("Add", number1 + number2)
#     case 2:
#         print("Subtract")
#     case 3:
#         print("Multiply", number1 * number2)
#     case 4:
#         print("Divide", number1 / number2)
#     case _:
#         print("Invalid Choice")



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# flag  = True

# while flag:

#     choise = int(input("""enter a choice of operation do you want to perform :
#                        1. Addition
#                        2.Subtraction
#                        3.Multiplication
#                        0.exit
#                          :"""))
    


# a=10
# b=20
# c=40
# def add(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b

# result=mul(sub(add(a,b),c),a)
# result=mul(sub(a,b),add(b,c))
# print(result)


# def double(number):
#     return number * 2

# def add_five(number):
#     return number + 5

# result = add_five(double(10))
# print(result)


# def demo():
#     print("A")
#     return 5
#     print("B")

# print(demo())


# def total(a, b, c=10):
#     return a + b + c

# print(total(1, c=3, b=2))


# def show(a, b=5):
#     print(a, b)

# show(10)
# show(10, 20)
# show(a=7, b=3)

# def add(*args):
#     print(args)
#     print(type(args))

# add(10, 20, 30)


# def calculate_area(length, width):
#     """
#     Calculate the area of a rectangle.

#     Args:
#         length: The rectangle's length.
#         width: The rectangle's width.

#     Returns:
#         The area of the rectangle.
#     """
#     return length * width
# print(calculate_area(2,4))

# print(calculate_area._doc_)

# def calculate():
#     total = 10
#     print(total)

# calculate()

# app_name = "StudyApp"

# def show_app():
#     print(app_name)

# show_app()
# print(app_name)

# x = 10

# def demo():
#     global x
#     print(x)
#     x = 20

# demo()
# print(x)


# count = 0 
# while count >=9:
    
#     print(count)
#     count+=




def outer():
    list="hi"
    def inner():
        print(list("hello"))
    inner()
outer()
