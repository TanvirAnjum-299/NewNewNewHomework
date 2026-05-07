import math
def circle_properties(radius):
    # Calculate area using formula: πr²
    area = math.pi * radius ** 2
    # Calculate perimeter (circumference) using formula: 2πr
    perimeter = 2 * math.pi * radius
    return area, perimeter
# Example usage
r = float(input("Enter the radius of the circle: "))
area, perimeter = circle_properties(r)

print(f"Area of the circle: {area:.2f}")
print(f"Perimeter of the circle: {perimeter:.2f}")
