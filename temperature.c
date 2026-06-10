#include <stdio.h>

// --- FUNCTION 1: Celsius to Fahrenheit ---
float to_fahrenheit(float celsius) {
    float result = (celsius * 9.0 / 5.0) + 32.0;
    return result; 
}

// --- FUNCTION 2: Fahrenheit to Celsius ---
float to_celsius(float fahrenheit) {
    float result = (fahrenheit - 32.0) * 5.0 / 9.0;
    return result; 
}

int main() {
    int choice;
    float input_temp, converted_temp;

    printf("=== Temperature Converter ===\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("Enter choice (1 or 2): ");
    scanf("%d", &choice);

    printf("Enter the temperature value: ");
    scanf("%f", &input_temp);

    // --- LOGIC AND FUNCTION CALLS ---
    if (choice == 1) {
        // Pass the input to to_fahrenheit and store the result
        converted_temp = to_fahrenheit(input_temp);
        printf("%.2f Celsius is equal to %.2f Fahrenheit\n", input_temp, converted_temp);
    } 
    else if (choice == 2) {
        // Pass the input to to_celsius and store the result
        converted_temp = to_celsius(input_temp);
        printf("%.2f Fahrenheit is equal to %.2f Celsius\n", input_temp, converted_temp);
    } 
    else {
        printf("Invalid choice! Please select 1 or 2.\n");
    }

    return 0;
}
