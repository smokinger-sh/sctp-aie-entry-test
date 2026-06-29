// Question 3 - String Manipulation
// Topic: Name Formatting Utility
//
// Task 1:
// Write a method called formatName(firstName, lastName) that accepts two Strings
// and returns a formatted String in this format: "lastName, firstName"
// Example: formatName("John", "Smith") → "Smith, John"
//
// Task 2:
// Write a method called formatInitials(firstName, lastName) that returns the
// initials of the person as a String in uppercase.
// Example: formatInitials("john", "smith") → "J.S."
// Note: your method should handle inputs in any case (upper, lower, or mixed)
// and always produce properly capitalised output.

public class Q3_java {

    public static String formatName(String firstName, String lastName) {
        // Capitalize first name
String formattedFirst =
        firstName.substring(0, 1).toUpperCase() +
        firstName.substring(1).toLowerCase();

// Capitalize last name
String formattedLast =
        lastName.substring(0, 1).toUpperCase() +
        lastName.substring(1).toLowerCase();

return formattedLast + ", " + formattedFirst;
    }

    public static String formatInitials(String firstName, String lastName) {
        String firstInitial =
        String.valueOf(firstName.charAt(0)).toUpperCase();

String lastInitial =
        String.valueOf(lastName.charAt(0)).toUpperCase();

return firstInitial + "." + lastInitial + ".";
    }

    public static void main(String[] args) {
        // Task 3: Call both methods with the following inputs and print each result:
        //   formatName("Alice", "Tan")    → Expected: "Tan, Alice"
        //   formatName("bob", "lim")      → Expected: "Lim, Bob"
        //   formatInitials("Alice","Tan") → Expected: "A.T."
        //   formatInitials("bob","lim")   → Expected: "B.L."

        System.out.println(formatName("Alice", "Tan"));
        System.out.println(formatName("bob", "lim"));
        System.out.println(formatInitials("Alice", "Tan"));
        System.out.println(formatInitials("bob", "lim"));
    }
}