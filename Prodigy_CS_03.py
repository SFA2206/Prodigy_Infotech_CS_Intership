import re

def assess_password_strength(password):
    # Initialize assessment
    assessment = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "numbers": False,
        "special_chars": False,
        "strength": 0,
        "feedback": ""
    }

    # Check length (min 8 chars)
    if len(password) >= 8:
        assessment["length"] = True

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        assessment["uppercase"] = True

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        assessment["lowercase"] = True

    # Check for numbers
    if re.search(r"\d", password):
        assessment["numbers"] = True

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        assessment["special_chars"] = True

    # Calculate strength score (0-5)
    assessment["strength"] = sum([
        assessment["length"],
        assessment["uppercase"],
        assessment["lowercase"],
        assessment["numbers"],
        assessment["special_chars"]
    ])

    # Provide feedback based on strength score
    if assessment["strength"] == 5:
        assessment["feedback"] = "Excellent password! You're Secure. Keep it up!"
    elif assessment["strength"] >= 3:
        assessment["feedback"] = "Good password! Consider adding more character types for extra security."
    else:
        assessment["feedback"] = "Weak password. Please add more character types and length for better security."

    return assessment

def main():
    password = input("Enter a password: ")
    assessment = assess_password_strength(password)

    print("Password Strength Assessment:")
    print(f"Length: {'Pass' if assessment['length'] else 'Fail'}")
    print(f"Uppercase: {'Pass' if assessment['uppercase'] else 'Fail'}")
    print(f"Lowercase: {'Pass' if assessment['lowercase'] else 'Fail'}")
    print(f"Numbers: {'Pass' if assessment['numbers'] else 'Fail'}")
    print(f"Special Characters: {'Pass' if assessment['special_chars'] else 'Fail'}")
    print(f"Strength Score: {assessment['strength']}/5")
    print(f"Feedback: {assessment['feedback']}")

if __name__ == "__main__":
    main()