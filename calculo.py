def calculate(num1, num2):
    """
    Returns product if product <= 1000, otherwise returns sum
    """
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Test cases
print("Case 1:")
number1 = 20
number2 = 30
result = calculate(number1, number2)
print(f"The result is {result}")

print("\nCase 2:")
number1 = 40
number2 = 30
result = calculate(number1, number2)
print(f"The result is {result}")
