def create_and_access_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Full Matrix:")
    for row in matrix:
        print(row)
    print("Accessed Elements:")
    print("First element:", matrix[0][0])
    print("Middle element:", matrix[1][1])
    print("Last element:", matrix[2][2])

# Display the results
create_and_access_matrix()
