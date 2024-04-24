def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Display the results
area, perimeter = rectangle_area_perimeter(5, 3)
print("Area:", area)
print("Perimeter:", perimeter)
