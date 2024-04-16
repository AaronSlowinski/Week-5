def linear_search_dictionary(dictionary, target):

    for key, value in dictionary.items():
        
        if value == target:
            
            print(f"Success: Found target value {target} at key {key}.")
            return key
    
    print(f"Failure: Target value {target} not found in the dictionary.")
    return None


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}

# Test the function with different target values
print(linear_search_dictionary(my_dictionary, 5))  
print(linear_search_dictionary(my_dictionary, 3))  
print(linear_search_dictionary(my_dictionary, 8))  
