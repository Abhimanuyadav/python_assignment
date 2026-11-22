#q1
choise=5
match choise:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")    
    case _:
        print("You selected Sandwich")    

#q2
settings=6

match settings:
    case 1:
        print("WI-FI")
    case 2:
        print(BLUETOOTH)  
    case 3:
        print("Mobaile Dataa")
    case 4:
        print("Airplane Mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid Settings")            

#q3
choice=6

match choice:
    case 1:
        print("Chech Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change Pin")
    case 5:
        print("Exit")
    case _:
        print("INvalid Choice")                    

#q4
color="blue"

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Color")        

#q5
choice=6

match choice:
    case 1:
        print("view profile")
    case 2:
        print("view courses")
    case 3:
        print("view marks")
    case 4:
        print("view attendance")
    case 5:
        print("Logout")
    case _:
        print("Invalid Choice")            


#q6
choice=6

match choice:
    case 1:
        print("electronccs")
    case 2:
        print("Cloting")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print(exit) 
    case _:
        print("Invalid Choice")                   

#q7
choice=6

match choice:

    case 1:
        print("Account Balance")
    case 2:
        print(" Mini Statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("Bill Payment")
    case 5:
        print("Customer Support")
    case _:
        print("Invalid Choice")

#q8
choice=5
match choice:
    case 1:
        print("Morning Show")
    case 2:
        print("Afternoon Show")
    case 3:
        print("Evening Show")
    case 4:
        print("Night Show") 
    case _:
        print("Invalid Choice")

#q9
n = input(
    "Enter Weather\n"
    "sunny\n"
    "rainy\n"
    "Cloudy\n"
    "Snowy\n"
    "Choice: "
).lower()

match n:
    case "Sunny":
        print("Wear sunglasses")
    case "Rainy":
        print("Take an umbrella")
    case "Cloudy":
        print("Carry a light jacket")
    case "Snowy":
        print("Wear warm clothes")
    case _:
        print("Invalid choice")

#q10
store = input(
    "Enter payment method:\n"
        "1. UPI\n"
    "2. Card\n"
    "3. Cash\n"
    "4. Wallet\n"
    "5. Another\n"
    "Choice: "
).lower()

match store:
    case "upi":
        print("UPI selected")
    case "card":
        print("Card selected")
    case "cash":
        print("Cash selected")
    case "wallet":
        print("Wallet selected")
    case "another":
        print("Another payment method selected")
    case _:
        print("Invalid payment method")

#q11
file_type = input(
    "Enter file type:\n"
    "1. pdf\n"
    "2. jpg\n"
    "3. png\n"
    "4. mp3\n"
    "5. mp4\n"
    "6. another\n"
    "Choice: "
)

match file_type:
    case "1":
        print("PDF")
    case "2":
        print("JPG")
    case "3":
        print("PNG")
    case "4":
        print("MP3")
    case "5":
        print("MP4")
    case "6":
        print("Another file type selected")
    case _:
        print("Invalid file type")

#q12
roles = input(
    "Enter role:\n"
    "1. admin\n"
    "2. teacher\n"
    "3. student\n"
    "4. guest\n"
    "Choice: "
).lower()

match roles:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Manage class")
    case "student":
        print("View course")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid role")

#q13
day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

#q14
priority=input("Enter number:")

match priority:
    case 1 | 2:
        print("Normal Priority:")
    case 3 | 4:
        print("Urgent Priority:")
    case _:
        print("other")

#q15
levels=input("Enter leaveals number:")

match levels:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("other")

#q16
account="student"
condition=2

match account:
    case "student":
        match condition:
            case 1:
                print("View Courses")
            case 2:
                print("View Marks")
            case _:
                print("View Attendance")
       
    case "teacher":
        match condition:
            case 1:
                print("View Students")
            case 2:
                print("Enter Marks")
            case _:
                print("View Attendance")
    case _:
        print("other persone")

#q17

account_type = int(input("Enter account type: "))
operation = int(input("Enter operation: "))


match account_type:
    case 1:
        print("Savings Account")
        
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case 2:
        print("Current Account")
    
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case _:
        print("Invalid Account Type")

#q18
category=int(input("enter category Number:"))
product=int(input("Enter product Number:"))

match category:
    case 1:
        print("Electronics")
        match product:
            case 1:
                print("Mobile")
            case 2:
                print("Laptop")
            case _:
                print("Headphones")
    case 2:
        print("Clothing")
        match product:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case _:
                print("Shoes")
    case _:
        print("Invalid category")

#q19
type_of_food=int(input("Enter Food Number:"))
type_of_menu=int(input("Enter Menu Number:"))

match type_of_food:
    case 1:
        print("Vegetarian")
        match type_of_menu:
            case 1:
                print("Paneer")
            case 2:
                print("Dal")
            case 3:
                print("Veg Biryani")
            case _:
                print("Invalid Menu")              
    case 2:
        print("Non-Vegetarian")
        match type_of_menu:
            case 1:
                print("Chicken Biryani")
            case 2:
                print("Chicken Curry")
            case 3:
                print("Fish Fry")      
            case _:
                print("Invalid Menu")      
    case _:
        print("Invalid Food")

#q20
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
op=input("Enter operator:")

match op:
    case "+":
        print(f"Result :{num1 + num2}")
    case "-":
        print(f"Result:{num1 - num2}")
    case "/":
        print(f"Result:{num1 / num2}")
    case "*":
        print(f"Result:{num1 * num2}")    
    case _:
        print(f"Inavalied operater:{op}")

