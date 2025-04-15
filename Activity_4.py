#1.Write a program that takes a person's age and prints the ticket price
age = int(input("Enter your age: "))
if age < 5:
    price = "Free"
elif 5 <= age <= 18:
    price = "₹100"
elif 19 <= age <= 60:
    price = "₹200"
else:  # age > 60
    price = "₹150"
print("Ticket Price:", price)



#2.Write a program to check login credentials. If username is "admin" and password is "1234", print "Login successful", else "Invalid credentials.
name = input("\n\nEnter username: ")
password = input("Enter password: ")
if name == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")



#3.Write a program to take marks as input and print grade.
marks = float(input("\n\nEnter your marks (0–100): "))
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
elif 0 <= marks < 60:
    grade = "F"
else:
    grade = "Invalid marks entered"
print("Your grade is:", grade)


#4.Take three numbers from the user and print the largest one.
a = float(input("\n\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("The largest number is:", largest)


