def check_divisibility(a, b):
    return a % b == 0 or b % a == 0

# Display the results
print("Is divisible:", check_divisibility(15, 5))
