def check_password_strength(password):
    score = 0
    remarks = ""

    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    special_characters = "!@#$%^&*()-_+=<>?/|\\{}[]~`"

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Character checks
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_symbol = True

    if has_lower:
        score += 1
    else:
        remarks += "Include at least one lowercase letter.\n"

    if has_upper:
        score += 1
    else:
        remarks += "Include at least one uppercase letter.\n"

    if has_digit:
        score += 1
    else:
        remarks += "Include at least one digit.\n"

    if has_symbol:
        score += 1
    else:
        remarks += "Include at least one special character (e.g. @, #, $, %, etc).\n"

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, remarks

# Main function
def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print("\nPassword Strength:", strength)
    if feedback:
        print("\nSuggestions to improve your password:")
        print(feedback)

# Run the program
if __name__ == "__main__":
    main()
