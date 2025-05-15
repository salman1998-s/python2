day_of_week = input("Enter the day of the week: ") .lower()
print(day_of_week)

if day_of_week == "Monday" or day_of_week == "Sunday":
 print("I will learn LIVE DevOps")
else :
 print("I will practic DevOps")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = input ("Enter your choice (+, -, *, /): ")

if choice == "+" :
 sum_of_num = int(num1) + (num2)
print ("Addition , sum_of_num")

if choice == "*" :
 product_of_num = int(num1) * int(num2)
 print ("Multiplication , product_of_num")

elif choice == "/" :
 division_of_num = int(num1) / int(num2)
 print ("Division , division_of_num")

else :
 print("Invalid choice")
# The code above is a simple calculator that performs addition, subtraction, multiplication, and division based on user input.
