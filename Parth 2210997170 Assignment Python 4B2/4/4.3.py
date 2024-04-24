def break_and_continue_demo():
    for i in range(1, 11):
        if i == 5:
            continue  # Skip the rest of the loop for i = 5
        if i == 8:
            break  # Exit the loop when i = 8
        print(i)

# Display the results
break_and_continue_demo()
