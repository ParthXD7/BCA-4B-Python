def list_methods_demo():
    my_list = [1, 2, 3, 2, 4, 2]
    my_list.append(5)
    print("Appended:", my_list)
    print("Count of 2s:", my_list.count(2))
    my_list.remove(2)
    print("After removing one occurrence of 2:", my_list)
    my_list.reverse()
    print("Reversed list:", my_list)
    my_list.sort()
    print("Sorted list:", my_list)

# Display the results
list_methods_demo()
