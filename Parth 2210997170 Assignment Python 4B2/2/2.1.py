def string_slices(sample_string):
    print("Sliced from 1 to 4:", sample_string[1:5])
    print("Sliced from start to 4:", sample_string[:5])
    print("Sliced from 5 to end:", sample_string[5:])
    print("Last three characters:", sample_string[-3:])

# Display the results
string_slices("Hello, Python!")
