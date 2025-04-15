#1. Function to Remove Specific Character from a String

def remove_char(s, char):
    return s.replace(char, '')
result = remove_char("hello", 'l')
print(result) 




#2. Function to Count Occurrences of a Character in a String
def count_char_occurrences(s, char):
    return s.count(char)
result = count_char_occurrences("hello", 'l')
print(result)  
