# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    try:
        return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    try:
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Main function for user interaction
def main():
    try:
        # Prompt user for temperature
        temp_input = input("Enter the temperature to convert: ")
        temp_value = float(temp_input)  # Convert input to float

        # Prompt user for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

# Run the script
if __name__ == "__main__":
    main()
