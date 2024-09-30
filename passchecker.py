import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    digit_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[\W_]', password)  # Non-alphanumeric characters

    # Initialize strength level and feedback
    strength_level = 0
    feedback = []

    # Check criteria and provide feedback
    if length_criteria:
        strength_level += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if lowercase_criteria:
        strength_level += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if uppercase_criteria:
        strength_level += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if digit_criteria:
        strength_level += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    if special_char_criteria:
        strength_level += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #).")

    # Determine strength based on the number of criteria met
    if strength_level == 5:
        return "Strong password!", feedback
    elif strength_level >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

def main():
    # Prompt user for password input
    password = input("Enter your password: ")
    
    # Check password strength
    strength, feedback = check_password_strength(password)
    
    # Display strength and feedback
    print(f"Password strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

# Run the main function when the program is executed
if __name__ == "__main__":
    main()
