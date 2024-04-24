def calculate_commission(sales_amount):
    if sales_amount >= 15000:
        return sales_amount * 0.20
    elif sales_amount >= 1000:
        return sales_amount * 0.15
    else:
        return sales_amount * 0.10

# Display the results
commission = calculate_commission(16000)
print("Commission:", commission)
