# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

def convertTemp(value, unit):
    # Check if the unit is Celsius
    if unit == "C":
        # Convert Celsius to Fahrenheit
        result = (value * 9 / 5) + 32
        # Round to 2 decimal places and return
        return round(result, 2)

    # Check if the unit is Fahrenheit
    elif unit == "F":
        # Convert Fahrenheit to Celsius
        result = (value - 32) * 5 / 9
        # Round to 2 decimal places and return
        return round(result, 2)

    # Return -1 for invalid unit
    else:
        return -1


# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

# Task 2: Call the function and print the results
print(convertTemp(100, "C"))
print(convertTemp(32, "F"))
print(convertTemp(37, "C"))
print(convertTemp("invalid", "X"))