# Part A
# Q1
while True:
    marks = float(input("Enter marks (between 0 and 100, inclusive): "))
    
    if 0 <= marks <= 100:
        break
    else:
        print("Invalid marks! Please enter a value between 0 and 100.")

print(f"Accepted marks: {marks}")



# Q2

while True:
    num = input("Enter a positive integer: ")

    try:
        num = int(num)
        if num > 0:
            print("Accepted number:", num)
            break
        else:
            print("Enter a number greater than 0.")
    except ValueError:
        print("Invalid input! Enter an integer.")


# Q3

while True:
    try:
        age = int(input("Enter your age: "))

        if 0 <= age <= 120:
            print("Accepted age:", age)
            break
        else:
            print("Error! Age must be between 0 and 120.")
    except ValueError:
        print("Enter a valid integer.")


# Q4

while True:
    print("\n1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice in [1, 2, 3, 4]:
            print("Selected option:", choice)
            break
        else:
            print("Invalid choice! Enter 1, 2, 3, or 4.")
    except ValueError:
        print("Enter an integer.")


# Q5

while True:
    password = input("Enter password: ").strip()

    if len(password) >= 8:
        print("Password accepted successfully!")
        break
    else:
        print("Password must contain at least 8 characters.")


# Q6

while True:
    try:
        temperature = float(input("Enter temperature (-20 to 45): "))

        if -20 <= temperature <= 45:
            print("Accepted temperature:", temperature)
            break
        else:
            print("Temperature must be between -20 and 45.")
    except ValueError:
        print("Enter a valid temperature.")


# Q7

balance = 5000

while True:
    try:
        withdrawal = float(input("Enter withdrawal amount: "))

        if 0 < withdrawal <= balance:
            balance = balance - withdrawal
            print("Remaining balance: ₹", balance)
            break
        else:
            print("Invalid amount! Check your balance.")
    except ValueError:
        print("Enter a valid amount.")


# Q8

while True:
    username = input("Enter username: ").strip()

    if len(username) >= 5 and " " not in username:
        print("Accepted username:", username)
        break
    else:
        print("Username must have at least 5 characters and no spaces.")


# Q9

while True:
    try:
        number = int(input("Enter a positive integer divisible by 3 and 5: "))

        if number > 0 and number % 3 == 0 and number % 5 == 0:
            print("Accepted number:", number)
            break
        else:
            print("Invalid! Enter a positive number divisible by both 3 and 5.")
    except ValueError:
        print("Enter an integer.")


# 10

secret_pin = "2468"
attempts = 0

while attempts < 3:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == secret_pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN!")

if attempts == 3 and pin != secret_pin:
    print("Access denied!")


# Q11

while True:
    try:
        value = int(input("Enter an integer between 10 and 50: "))

        if 10 <= value <= 50:
            if value % 2 == 0:
                print(value, "is even.")
            else:
                print(value, "is odd.")
            break
        else:
            print("Enter a number between 10 and 50.")
    except ValueError:
        print("Enter a valid integer.")


#Q12

balance = 2000

while True:
    try:
        deposit = float(input("Enter deposit amount: "))

        if deposit > 0:
            balance = balance + deposit
            print("New balance: ₹", balance)
            break
        else:
            print("Deposit must be greater than 0.")
    except ValueError:
        print("Enter a valid amount.")



# 13
print("=== Problem 13: Integer Between 1 and 100 ===")
while True:
    num = int(input("Enter an integer between 1 and 100: "))
    if 1 <= num <= 100:
        print(f"Valid number accepted: {num}\n")
        break
    print("Invalid! Number must be between 1 and 100. Try again.")


# 14
print("=== Problem 14: Marks and Result ===")
while True:
    marks = float(input("Enter marks (0 to 100): "))
    if 0 <= marks <= 100:
        break
    print("Invalid marks! Please enter a value between 0 and 100.")

if marks >= 75:
    print("Result: Distinction\n")
elif marks >= 60:
    print("Result: First Class\n")
elif marks >= 35:
    print("Result: Pass\n")
else:
    print("Result: Fail\n")


# 15
print("=== Problem 15: Username and Password Validation ===")
while True:
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    
    is_valid_username = len(username) >= 5 and " " not in username
    
    
    is_valid_password = len(password) >= 8 and password.strip() != ""

    if is_valid_username and is_valid_password:
        print("Success! Both username and password are valid.\n")
        break
    else:
        print("Validation failed. Please check the rules and try again:")
        if not is_valid_username:
            print("- Username must be at least 5 characters and contain no spaces.")
        if not is_valid_password:
            print("- Password must be at least 8 characters and not blank.")


#16
print("=== Problem 16: Calculator Input Validation ===")
num1 = float(input("Enter first number: "))

while True:
    operator = input("Enter operator (+, -, *, /): ").strip()
    if operator in ('+', '-', '*', '/'):
        break
    print("Invalid operator! Please choose from +, -, *, /.")

while True:
    num2 = float(input("Enter second number: "))
    if operator == '/' and num2 == 0:
        print("Error: Division by zero is not allowed. Enter the second number again.")
        continue
    break

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

print(f"Result: {num1} {operator} {num2} = {result}\n")


# 17
print("=== Problem 17: Banking Menu ===")
balance = 10000

while True:
    print("\n--- Banking Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        print(f"Current Balance: ₹{balance}")
    elif choice == 2:
        deposit = float(input("Enter deposit amount: ₹"))
        if deposit > 0:
            balance += deposit
            print(f"Deposited successfully! New Balance: ₹{balance}")
        else:
            print("Invalid deposit amount. Must be greater than zero.")
    elif choice == 3:
        withdrawal = float(input("Enter withdrawal amount: ₹"))
        if 0 < withdrawal <= balance:
            balance -= withdrawal
            print(f"Withdrawal successful! Remaining Balance: ₹{balance}")
        else:
            print("Invalid withdrawal amount (must be positive and not exceed balance).")
    elif choice == 4:
        print("Exiting Banking System. Goodbye!\n")
        break
    else:
        print("Invalid menu choice! Please select between 1 and 4.")


# 18
print("=== Problem 18: Validate Month and Day ===")
while True:
    month = int(input("Enter month number (1-12): "))
    day = int(input("Enter day number (1-31): "))
    
    if 1 <= month <= 12 and 1 <= day <= 31:
        print(f"Valid date entered: Month {month}, Day {day}\n")
        break
    print("Invalid month or day range! Please try again.")


# 19
print("=== Problem 19: Product Quantity and Price ===")
while True:
    quantity = int(input("Enter product quantity (positive integer): "))
    if quantity > 0:
        break
    print("Invalid quantity! Must be a positive integer.")

while True:
    unit_price = float(input("Enter unit price (greater than zero): "))
    if unit_price > 0:
        break
    print("Invalid price! Must be greater than zero.")

total_cost = quantity * unit_price
print(f"Total Cost: ₹{total_cost:.2f}\n")


# 20
print("=== Problem 20: Safe Average Calculator ===")
while True:
    count = int(input("How many numbers do you want to enter (1 to 20)? "))
    if 1 <= count <= 20:
        break
    print("Invalid count! Must be between 1 and 20.")

total_sum = 0
for i in range(count):
    while True:
        val = float(input(f"Enter value {i+1}: "))
        
        if 0 <= val <= 100:
            total_sum += val
            break
        print("Value out of range (0-100). Try again.")

average = total_sum / count
print(f"The average is: {average:.2f}\n")


# 21
print("=== Problem 21: Stronger Password Rules ===")
while True:
    pwd = input("Enter strong password: ")
    
    has_length = len(pwd) >= 8
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    no_space = not any(c.isspace() for c in pwd)
    
    if has_length and has_upper and has_lower and has_digit and no_space:
        print("Password meets all security criteria!\n")
        break
    
    print("Password validation failed. Rules not met:")
    if not has_length: print("- Must be at least 8 characters.")
    if not has_upper: print("- Must contain at least one uppercase letter.")
    if not has_lower: print("- Must contain at least one lowercase letter.")
    if not has_digit: print("- Must contain at least one digit.")
    if not has_space: print("- Must not contain whitespace characters.")


# 22
print("=== Problem 22: Input Validation Without break ===")
val = 0
while not (1 <= val <= 10):
    val = int(input("Enter an integer from 1 to 10: "))
    if not (1 <= val <= 10):
        print("Invalid value, try again.")
print(f"Valid integer accepted: {val}\n")


# 23
print("=== Problem 23: Three Valid Scores ===")
scores = []
for i in range(1, 4):
    while True:
        score = float(input(f"Enter score {i} (0 to 100): "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        print("Invalid score! Must be between 0 and 100.")

total_score = sum(scores)
avg_score = total_score / len(scores)
print(f"Total Score: {total_score}, Average Score: {avg_score:.2f}\n")


# 24
print("=== Problem 24: ATM Withdrawal With Denomination Rules ===")
atm_balance = 10000

while True:
    withdrawal_amt = float(input("Enter withdrawal amount (multiples of ₹100): ₹"))
    
    if withdrawal_amt <= 0:
        print("Error: Amount must be positive.")
    elif withdrawal_amt > atm_balance:
        print("Error: Amount exceeds available balance (₹10000).")
    elif withdrawal_amt % 100 != 0:
        print("Error: Amount must be a multiple of ₹100.")
    else:
        atm_balance -= withdrawal_amt
        print(f"Successfully withdrawn: ₹{withdrawal_amt}")
        print(f"Remaining Balance: ₹{atm_balance}\n")
        break