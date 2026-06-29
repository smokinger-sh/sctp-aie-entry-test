// Question 3 - String Manipulation
// Topic: Name Formatting Utility
//
// Task 1:
// Write a function called formatName(firstName, lastName) that accepts two strings
// and returns a formatted string in this format: "lastName, firstName"
// Example: formatName("John", "Smith") → "Smith, John"

function formatName(firstName, lastName) {
    firstName = firstName.charAt(0).toUpperCase() + firstName.slice(1).toLowerCase();
    lastName = lastName.charAt(0).toUpperCase() + lastName.slice(1).toLowerCase();

    return lastName + ", " + firstName;
}


// Task 2:
// Write a function called formatInitials(firstName, lastName) that returns the
// initials of the person as a string in uppercase.
// Example: formatInitials("john", "smith") → "J.S."
// Note: your function should handle inputs in any case (upper, lower, or mixed)
// and always produce properly capitalised output.

function formatInitials(firstName, lastName) {
    return firstName.charAt(0).toUpperCase() + "." +
           lastName.charAt(0).toUpperCase() + ".";
}


// Task 3:
// Call both functions with the following inputs and print each result:
//   formatName("Alice", "Tan")    → Expected: "Tan, Alice"
//   formatName("bob", "lim")      → Expected: "Lim, Bob"
//   formatInitials("Alice","Tan") → Expected: "A.T."
//   formatInitials("bob","lim")   → Expected: "B.L."

console.log(formatName("Alice", "Tan"));
console.log(formatName("bob", "lim"));
console.log(formatInitials("Alice", "Tan"));
console.log(formatInitials("bob", "lim"));