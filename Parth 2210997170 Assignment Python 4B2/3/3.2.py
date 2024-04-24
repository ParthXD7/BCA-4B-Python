def number_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Display the results
print("Number sign:", number_sign(-10))
