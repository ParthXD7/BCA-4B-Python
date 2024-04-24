def print_indexes():
    elements = ['q', 'w', 'e', 'r', 't', 'y']
    for i in range(len(elements)):
        print(f"Element: {elements[i]}, Positive index: {i}, Negative index: {-len(elements) + i}")

# Display the results
print_indexes()
