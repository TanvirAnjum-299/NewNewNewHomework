def is_disarium(num):
    # Convert number to string to access digits with positions
    digits = str(num)
    length = len(digits)
    
    # Calculate sum of digits powered by their positions
    total = 0
    for i in range(length):
        total += int(digits[i]) ** (i + 1)
    
    # Check if sum equals the original number
    return total == num

# Main program
number = int(input("Enter a number: "))
if is_disarium(number):
    print(number, "is a Disarium number.")
else:
    print(number, "is not a Disarium number.")