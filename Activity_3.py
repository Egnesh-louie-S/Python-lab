#1.Write a Python program that takes a number from the user and checks whether it is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("\nEnter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#2.Write a Python program to print the multiplication table of a given number using a for loop
n = int(input("\nEnter a number: "))
print(f"Multiplication Table for {n}:")
for i in range(1, 11):  # Loop from 1 to 10
    print(f"{n} x {i} = {n * i}")   


#3.Write a Python program to find the sum of digits of a number using a while loop.
num = int(input("\nEnter the number to sum its digits: "))
sums= 0
while num > 0:
    sums+= num % 10  
    num //= 10  
print("Sum of digits: ",sums)



#4.Write a Python program to create a list of squares of all even numbers from 1 to 20 using list comprehension, and then calculate the sum of all those squares.
sqt= [n**2 for n in range(1, 21) if n % 2 == 0]
sum_of_squares = sum(sqt)
print("\nList of squares of even numbers:", sqt)
print("Sum of all squares:", sum_of_squares)

