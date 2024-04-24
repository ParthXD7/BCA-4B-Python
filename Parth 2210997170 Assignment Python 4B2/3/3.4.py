def calculate_allowances(basic_salary):
    if basic_salary >= 20000:
        da = basic_salary * 0.30
        hra = basic_salary * 0.20
    else:
        da = basic_salary * 0.20
        hra = basic_salary * 0.10
    return da, hra

# Display the results
da, hra = calculate_allowances(25000)
print("DA:", da, "HRA:", hra)
