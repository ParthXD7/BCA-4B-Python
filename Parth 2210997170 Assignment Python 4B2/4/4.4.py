def else_with_while():
    count = 1
    while count <= 5:
        print(count)
        count += 1
        if count == 4:
            break
    else:
        print("Reached end of loop")

# Display the results
else_with_while()
