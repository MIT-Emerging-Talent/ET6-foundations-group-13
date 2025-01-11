# Function that converts celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Converts the inputted temperature from Celsius to Fahrenheit.

    Input: Value in Celsius
    Output: Value in Fahrenheit
    """
    return (celsius * 9 / 5) + 32


# Get user input
celsius = float(input("Enter temperature in Celsius: "))

# Call the function and get the Fahrenheit value
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F.")
# Program that converts  Celsius to Fahrenheit
