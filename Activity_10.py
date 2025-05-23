#1: You are given a list of customer IDs with duplicates. Remove the duplicates.
customer_ids = [101, 102, 103, 101, 104, 102]
unique_customer_ids = list(set(customer_ids))
print(unique_customer_ids)


#2: Two stores have customer records. Find customers who shopped at both stores.
store1_customers = {"Alice", "Bob", "Charlie", "David"}
store2_customers = {"Eve", "Bob", "David", "Frank"}
common_customers = store1_customers & store2_customers
print(common_customers)


#3: Find customers who bought a product but never returned.
all_customers = {"John", "Mary", "Steve", "Ana"}
returned_customers = {"Mary", "Ana"}
non_returning_customers = all_customers - returned_customers
print('customers not returned the products',non_returning_customers)


#4: Check whether a sentence has duplicate words.
sentence = "the sky is blue and the grass is green"
words = sentence.split()
has_duplicates = len(words) != len(set(words))
print("Has duplicates:", has_duplicates)


#5: A warehouse is supposed to have items A–E. Find out which ones are missing.
expected_items = {"A", "B", "C", "D", "E"}
available_items = {"A", "C", "E"}
missing_items = expected_items - available_items
print('missing warehouses:',missing_items)
