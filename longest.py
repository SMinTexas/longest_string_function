# Write a function that accepts a list of strings as an argument.
# It should return the longest string in the list.

def longest(string_list):
    longest_string = max(string_list, key=len)
    return longest_string

list_of_strings = ["Howdy", "Aggies", "Clemson", "Going", "Down", "Saturday"]
 
print(" ")
print(f"Original List of Words: {list_of_strings}")
print(" ")
print(f"Longest String: {longest(list_of_strings)}")
print(" ")