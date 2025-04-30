# Initialize an empty list to store student names
students = []

# Loop to input names of 10 students
for i in range(10):
    name = input(f"Enter name of student {i+1}: ")
    
    # Ensure name length is not more than 15 characters
    name = name[:15]  # Slice to first 15 characters if it's longer
    students.append(name)

# Display names in reverse order
print("\nReversed Names:")
for name in students:
    print(name[::-1])  # Reverse the string using slicing
