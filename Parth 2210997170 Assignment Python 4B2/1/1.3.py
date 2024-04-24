def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

# Display the results
total_amount = compound_interest(1000, 5, 3)
print("Compound Interest:", total_amount)
