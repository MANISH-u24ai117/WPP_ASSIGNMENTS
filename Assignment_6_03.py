class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()

        # Conversion factors for each unit to meters
        self.conversion_factors = {
            'inches': 0.0254,  # 1 inch = 0.0254 meters
            'feet': 0.3048,    # 1 foot = 0.3048 meters
            'yards': 0.9144,   # 1 yard = 0.9144 meters
            'miles': 1609.34,  # 1 mile = 1609.34 meters
            'kilometers': 1000, # 1 kilometer = 1000 meters
            'meters': 1,       # 1 meter = 1 meter
            'centimeters': 0.01, # 1 cm = 0.01 meters
            'millimeters': 0.001 # 1 mm = 0.001 meters
        }

        # Check if the unit is valid
        if self.unit not in self.conversion_factors:
            raise ValueError("Invalid unit. Choose from: inches, feet, yards, miles, kilometers, meters, centimeters, millimeters.")

    def to_meters(self):
        # Convert the given length to meters
        return self.length * self.conversion_factors[self.unit]

    def inches(self):
        # Convert length to inches
        return self.to_meters() / self.conversion_factors['inches']

    def feet(self):
        # Convert length to feet
        return self.to_meters() / self.conversion_factors['feet']

    def yards(self):
        # Convert length to yards
        return self.to_meters() / self.conversion_factors['yards']

    def miles(self):
        # Convert length to miles
        return self.to_meters() / self.conversion_factors['miles']

    def kilometers(self):
        # Convert length to kilometers
        return self.to_meters() / self.conversion_factors['kilometers']

    def meters(self):
        # Return length in meters (already in meters after conversion)
        return self.to_meters()

    def centimeters(self):
        # Convert length to centimeters
        return self.to_meters() / self.conversion_factors['centimeters']

    def millimeters(self):
        # Convert length to millimeters
        return self.to_meters() / self.conversion_factors['millimeters']

# Example Usage:
c = Converter(9, 'inches')

print(c.feet())         # Output: 0.75
print(c.yards())        # Output: 0.25
print(c.miles())        # Output: 0.000142857
print(c.kilometers())   # Output: 0.0002286
