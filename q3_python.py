# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    # Capitalize the first letter of each name
    firstName = firstName.capitalize()
    lastName = lastName.capitalize()

    # Return in the format "lastName, firstName"
    return lastName + ", " + firstName


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    # Get the first letter of each name and convert to uppercase
    firstInitial = firstName[0].upper()
    lastInitial = lastName[0].upper()

    # Return the initials in the format "A.T."
    return firstInitial + "." + lastInitial + "."

# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

print(formatName("Alice", "Tan"))
print(formatName("bob", "lim"))
print(formatInitials("Alice", "Tan"))
print(formatInitials("bob", "lim"))