# Create a function to generate equivalence classes modulo 5 for numbers 1 to 10000
def equivalence_classes_modulo_5():
    # Create 5 empty lists for the equivalence classes
    equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

    # Iterate through numbers 1 to 10000
    for number in range(1, 10001):
        remainder = number % 5
        equivalence_classes[remainder].append(number)

    return equivalence_classes

# Generate equivalence classes
equivalence_classes = equivalence_classes_modulo_5()

# Check validity: Union of all equivalence classes should be the set {1, 2, ..., 10000}
all_numbers = set(range(1, 10001))
union_of_classes = set()
for cls in equivalence_classes.values():
    union_of_classes.update(cls)

# Check if the union covers all numbers from 1 to 10000
if union_of_classes == all_numbers:
    print("The equivalence classes are valid. The union of all classes is the original set.")
else:
    print("There is an issue with the equivalence classes.")

# Optionally, print the equivalence classes for inspection (optional)
for remainder, cls in equivalence_classes.items():
    print(f"Equivalence class for remainder {remainder} (mod 5): {cls[:10]}...")  # Print the first 10 elements for brevity
