

# c

# Create a function that takes a list of items and checks if the last item matches the rest of the list concatenated together.
# Examples

# match_last_item(["rsq", "6hi", "g", "rsq6hig"]) ➞ True
# # The last item is the rest joined.

# match_last_item([1, 1, 1, "11"]) ➞ False
# # The last item should be "111".

# match_last_item([8, "thunder", True, "8thunderTrue"]) ➞ True

# Notes

# The list is always filled with items.



def match_last_item(lst):
    # Remove the last element from the list and store it
    removed_element = lst.pop(-1)
    
    # Join the rest of the elements as strings and compare with the removed element
    if "".join(map(str, lst)) == str(removed_element):
        return True
    else:
        return False

# Test the function
print(match_last_item(["rsq", "6hi", "g", "rsq6hig"]))  # True



def match_last_item(lst):
    # Concatenate all elements except the last one
    concatenated = ''.join(map(str, lst[:-1]))
    
    # Check if the concatenated string equals the last element
    return concatenated == str(lst[-1])

# Test the function
print(match_last_item(["rsq", "6hi", "g", "rsq6hig"]))  # True




def match_last_item(lst):
    # Concatenate all elements except the last one as strings
    concatenated = ''.join(map(str, lst[:-1]))
    
    # Check if the last item matches the concatenated result
    return concatenated == str(lst[-1])

# Test cases
test_cases = [
    (["rsq", "6hi", "g", "rsq6hig"]),  # True
    ([1, 1, 1, "11"]),  # False
    ([8, "thunder", True, "8thunderTrue"])  # True
]

results = {str(test): match_last_item(test) for test in test_cases}
results
