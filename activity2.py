
""" Checks if a string is a palindrome (reads the same backward as forward). """
def is_palindrome(s):

   return s == s[::-1]


string1 = "racecar"
print("This is palindrome:",is_palindrome(string1)) 

string2 = "hello"
print("This is palindrome:",is_palindrome(string2))





""" This function takes a list of numbers and returns the largest number.  """
def find_largest(lst):
  if not lst:
      return None  
  largest = lst[0]
  for number in lst:
      if number > largest:
          largest = number
  return largest

numbers = [10, 20, 35, 8, 25, 83]
print("\nLargest number is:",find_largest(numbers))




""" This function counts the number of vowels (a, e, i, o, u) in a given string.         """
def count_vowels(s):

   vowels = "aeiouAEIOU"
   count = 0
   for char in s:
       if char in vowels:
           count += 1
   return count
print("\nNumber of vowels are:",count_vowels("Hello Everyone"))
print("Number of vowels are:",count_vowels("Python"))  
print("Number of vowels are:",count_vowels("Wonderful Day"))



