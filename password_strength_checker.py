import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc).")

    # Evaluate strength
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter your password to check its strength: ")
    strength, suggestions = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
