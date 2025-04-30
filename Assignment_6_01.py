class Password_manager:
    def __init__(self):
        # Initialize an empty list to store the user's past passwords
        self.old_passwords = []

    def get_password(self):
        # Return the current password (the last item in the list)
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            return None  # No password has been set yet
    
    def set_password(self, new_password):
        # Check if the new password is different from all previous passwords
        if new_password not in self.old_passwords:
            # Set the new password by adding it to the list
            self.old_passwords.append(new_password)
        else:
            print("This password has been used before. Please choose a different one.")
    
    def is_correct(self, password):
        # Check if the input password is equal to the current password
        return password == self.get_password()

# Example Usage
pm = Password_manager()
pm.set_password("mySecurePass123")  # Set a new password
print(pm.get_password())  # Output: mySecurePass123

pm.set_password("anotherPassword456")  # Set a different password
print(pm.is_correct("mySecurePass123"))  # Output: False
print(pm.is_correct("anotherPassword456"))  # Output: True

pm.set_password("mySecurePass123")  # Attempt to reuse a previous password (should not work)
