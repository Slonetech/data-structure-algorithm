def remove_duplicates(sequence):
    unique_elements = set() # Create an empty set
    result = [] # Create an empty list to store the result
    
    for element in sequence:
        if element not in unique_elements: # If element is not in the set
            result.append(element) # Add it to the result list
            unique_elements.add(element) # Add it to the set
    
    return result # Return the result list

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
