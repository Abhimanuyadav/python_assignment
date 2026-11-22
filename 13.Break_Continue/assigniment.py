# # Q1 A1
# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")
#output
# 1
# 2
# 3
# 4
# Finished


# Q2
# word = "skyline"
# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)
# output
# s
# K
# y
# l

# # Q3. 
# n = 2
# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2
# output
# 2
# 4
# 6


# # Q4. A2
# limit = int(input("Enter limit: "))
# for i in range(1, limit + 1):
#     if i == 7:
#         break
#     print(i, end=" ")


# # Q5
# word = input("Enter string: ")
# target = input("Enter target character: ")
# for ch in word:
#     print(ch, end=" ")
#     if ch == target:
#         break


# # Q6
# num=input("Enter a number: ").split()
# for i in num:
#     if int(i)<0:
#         break
#     print(i)

# # Q7 A3
# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)
# output
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


# # Q8
# sentence = input("Enter sentence: ").split()
# target = input("Enter target word: ")
# for word in sentence:
#     if word == target:
#         print("Found")
#         break
# else:
#     print("Not found")


# # Q9 B1
# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)
# output
# 1
# 2
# 3
# 5
# 6

# # Q10
# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")
# output
# dctn

# # Q11
# n = 0
# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)
# 1
# 2
# 3
# 4
# 5



# # Q12 B2
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")


# # Q13
# word = input("Enter string: ")
# target = input("Enter character: ")
# for ch in word:
#     if ch == target:
#         continue
#     print(ch, end="")


# # Q14
# marks = list(map(int, input("Enter marks: ").split()))
# for mark in marks:
#     if mark < 40:
#         continue
#     print(mark, end=" ")


# # Q15 B3
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)
# OUTPUT
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4

# # Q16
# n = 0
# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)
# output
# 1
# 2
# 4
# 5


# # Q17
# word = input("Enter word: ")
# count = 0
# for ch in word.lower():
#     if ch in "aeiou":
#         continue
#     count += 1
# print(count)


# # Q18 C1
# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")
# OUTPUT
# 1
# 2
# 4
# 5


# # Q19
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")
# OUTPUT
# 1
# 3
# 4
# Completed


 # # Q20
# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")
# OUTPUT
# 1
# 2
# Outside loop


# # Q21
# for item in []:
#     print("Inside")
# else:
#     print("Else block")
# OUTPUT
# Else block

# # Q22  C2
# numbers = list(map(int, input("Enter numbers: ").split()))
# target = int(input("Enter target: "))
# for n in numbers:
#     if n == target:
#         print("Found")
#         break
# else:
#     print("Not found")


# # Q23
# word = input("Enter string: ")
# target = input("Enter character: ")
# for ch in word:
#     if ch == target:
#         print("Character exists")
#         break
# else:
#     print("Character missing")


# # Q24
# n = int(input("Enter number: "))
# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")


# # Q25 C3
# values = [2, 4, 6, 8]
# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")
# OUTPUT
# All are even


# # Q26 A
# for x in range(3):
#     continue
# else:
#     print("A")
# OUTPUT
# A

 # # Q26 B 
# for x in range(3):
#     break
# else:
#     print("B")

# # Q26. C
# for x in range(0):
#     print(x)
# else:
#     print("C")
# OUTPUT
# C

# # Q27.
# word = input("Enter string: ")
# for ch in word:
#     if word.count(ch) >= 2:
#         print(ch)
#         break
# else:
#     print("No repeated character")


# # Q28. 
# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)


# # Q29. 
# x = 10
# if x > 5:
#     pass
# print("Finished")


# # Q30
# for letter in "cat":
#     pass
# print("Loop ended")


# # Q31
# for i in range(1, 6):
#     if i % 2 == 0:
#         pass
#     print(i, end=" ")


# # Q32
# choice = int(input("Enter choice: "))
# if choice == 1:
#     print("Option 1 selected")
# elif choice == 2:
#     pass
# else:
#     print("Unknown option")
# print("Program closed")


# # Q33
# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

# # Q33
# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)


# # Q34
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)