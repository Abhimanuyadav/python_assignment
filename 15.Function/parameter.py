# #Beginner
# #1
# def welcome():
#     print("Welcome to Python")

# welcome()
# welcome()
# welcome()
# print()

# #2
# def greet(name):
#     print("Hello", name)

# greet("Asha")
# print()


# #3
# def show_number(number):
#     print(number)

# show_number(42)
# print()

# #4
# def add(a, b):
#     return a + b

# result = add(10, 5)
# print("Sum:", result)
# print()


# #5
# def square(number):
#     return number * number

# print("Square of 6:", square(6))
# print()


# 6
def is_even(number):
    return number % 2 == 0

print("--- Beginner ---")
print("is_even(4):", is_even(4))       
print("is_even(7):", is_even(7))       


# 7
def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

print("get_full_name:", get_full_name("Asha", "Patel"))


# 8
def introduce(name, city="Pune"):
    print(f"Name: {name}, City: {city}")

print("introduce tests:")
introduce("Asha", "Mumbai")  
introduce("Rahul")           


# 9
def subtract(a, b):
    return a - b

print("subtract(10, 3):", subtract(10, 3))   
print("subtract(3, 10):", subtract(3, 10))   

# 10
def get_min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a

print("get_min_max(12, 5):", get_min_max(12, 5))



# 2. INTERMEDIATE 

# 11
def calculate(a, b):
    return a + b, a - b, a * b, a / b

print("\n--- Intermediate ---")
print("calculate(10, 2):", calculate(10, 2))


# 12
def count_digits(number):
    if number == 0:
        return 1
    count = 0
    number = abs(number)
    while number > 0:
        count += 1
        number //= 10
    return count

print("count_digits(0):", count_digits(0))
print("count_digits(12345):", count_digits(12345))


# 13
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print("classify_number(-5):", classify_number(-5))


# 14
def calculate_total(price, quantity=1):
    return price * quantity

print("calculate_total(50, 3):", calculate_total(50, 3))


# 15
def create_email(username, domain="example.com"):
    return f"{username}@{domain}"

print("create_email('john'):", create_email("john"))


# 16
def format_name(first, last, uppercase=False):
    full = f"{first} {last}"
    return full.upper() if uppercase else full

print("format_name('john', 'doe', True):", format_name("john", "doe", True))


# 17
def percentage(marks, total=100):
    return (marks / total) * 100

print("percentage(45, 50):", percentage(45, 50))


# 18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

print("convert_minutes(5):", convert_minutes(5))


# 19
def student_details(name, age, city):
    print(f"Student: {name}, Age: {age}, City: {city}")

print("student_details keyword call:")
student_details(city="Delhi", name="Rohan", age=22)


# 20
def bill(item, quantity=1, price=100):
    return f"{item}: {quantity} pcs @ {price} each = Total: {quantity * price}"

print("bill positional:", bill("Pen", 5, 10))
print("bill keyword:", bill(item="Notebook", price=50))



# 3. CHALLENGING 

# 21
def analyze_number(number):
    absolute = -number if number < 0 else number
    is_even_val = (number % 2 == 0)
    digits = count_digits(number)
    return absolute, is_even_val, digits

print("\n--- Challenging ---")
print("analyze_number(-45):", analyze_number(-45))


# 22
def calculate_stats(a, b, c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    total_sum = a + b + c
    return smallest, largest, total_sum

print("calculate_stats(4, 9, 2):", calculate_stats(4, 9, 2))


# 23
def make_sentence(subject, verb, object):
    return f"{subject} {verb} the {object}."

print("make_sentence with keywords:", make_sentence(object="apple", subject="Boy", verb="eats"))


# 24
def apply_discount(price, discount=0):
    return price - (price * (discount / 100))

print("apply_discount(1000, 20):", apply_discount(1000, 20))


# 25
def calculate_pay(hours, rate=200, bonus=0):
    return (hours * rate) + bonus

print("calculate_pay(40):", calculate_pay(40))
print("calculate_pay(hours=30, bonus=500):", calculate_pay(hours=30, bonus=500))


# 26
def get_coordinates(x=0, y=0):
    return x, y

print("get_coordinates():", get_coordinates())
print("get_coordinates(y=15):", get_coordinates(y=15))


# 27
def compare(a, b):
    if a > b:
        relation = "A is greater"
        diff = a - b
    elif b > a:
        relation = "B is greater"
        diff = b - a
    else:
        relation = "Equal"
        diff = 0
    return relation, diff

print("compare(10, 25):", compare(10, 25))


# 28
def convert_temperature(value, scale="C"):
    if scale == "C":
        return (value * 9/5) + 32  
    elif scale == "F":
        return (value - 32) * 5/9  
    return value

print("convert_temperature(0, 'C'):", convert_temperature(0, 'C'))
print("convert_temperature(32, 'F'):", convert_temperature(32, 'F'))


# 29
def calculate_result(marks, passing_marks=35):
    return "Pass" if marks >= passing_marks else "Fail"

print("calculate_result(40):", calculate_result(40))
print("calculate_result(30, 35):", calculate_result(30, 35))


# 30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return (quantity * price) + delivery_fee

print("order_summary changing only delivery fee:", order_summary("Shoes", delivery_fee=80))