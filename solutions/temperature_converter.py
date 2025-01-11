# Function that converts Celsius to Fahrenheit
def temperature_converter(celsius):
    """
    Converts the inputted temperature from Celsius to Fahrenheit.

    Input: Value in Celsius
    Output: Value in Fahrenheit
    """
    return (celsius * 9 / 5) + 32


# Ensure this code block only executes when the script is run directly
if __name__ == "__main__":
    # Get user input
    celsius = float(input("Kindly Enter temperature in Celsius: "))

    # Call the function and get the Fahrenheit value
    fahrenheit = temperature_converter(celsius)

    # Display the result
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
