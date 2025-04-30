def convert_length(feet, option):
    # Conversion factors for feet
    conversions = [
        feet * 12,           # Inches
        feet / 3,            # Yards
        feet / 5280,         # Miles
        feet * 304.8,        # Millimeters
        feet * 30.48,        # Centimeters
        feet * 0.3048,       # Meters
        feet * 0.0003048     # Kilometers
    ]
    return conversions[option - 1]

# Main program
print("Enter a length in feet:")
feet = float(input())

print("Choose a conversion option:")
print("1: Inches")
print("2: Yards")
print("3: Miles")
print("4: Millimeters")
print("5: Centimeters")
print("6: Meters")
print("7: Kilometers")

option = int(input())

# Check if the option is valid
if 1 <= option <= 7:
    result = convert_length(feet, option)
    print(f"{feet} feet is equal to {result} in the chosen unit.")
else:
    print("Invalid option. Please choose a number between 1 and 7.")
