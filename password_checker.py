# Display a title so the user knows what this program does.
print("Password Strength Checker")

# Load the list of commonly used passwords from the text file.
# splitlines() turns each line in the file into one item in the list.
with open("common_passwords.txt", "r") as file:
    common_passwords = file.read().splitlines()

# Keep asking until the password passes every requirement.
while True:
    password = input("Enter your password: ")

    # Check each password requirement. any() returns True when at least one
    # character matches the condition inside the parentheses.
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # Calculate the two checks that need a little extra logic.
    is_common = password.lower() in common_passwords
    has_no_spaces = not any(char.isspace() for char in password)

    # The password is valid only when every requirement is True.
    is_valid = (
        bool(password)
        and has_no_spaces
        and len(password) >= 12
        and has_uppercase
        and has_lowercase
        and has_number
        and has_symbol
        and not is_common
    )

    # Show the result of each individual password check.
    print("\nPassword information:")
    print("Has uppercase letter:", has_uppercase)
    print("Has lowercase letter:", has_lowercase)
    print("Has number:", has_number)
    print("Has symbol:", has_symbol)
    print("Contains spaces:", not has_no_spaces)
    print("Common password:", is_common)

    # Give the password 20 points for each strength requirement it meets.
    score = sum(
        [len(password) >= 12, has_uppercase, has_lowercase, has_number, has_symbol]
    ) * 20

    # A common password should never receive a positive strength score.
    if is_common:
        score = 0

    # Convert the numeric score into an easy-to-understand rating.
    if score >= 80:
        rating = "strong"
    elif score >= 60:
        rating = "moderate"
    else:
        rating = "weak"
    print("Score:", score, "/ 100")
    print("Password rating:", rating)

    # Build a list of specific improvements for requirements that failed.
    suggestions = []
    if not has_uppercase:
        suggestions.append("Add uppercase letter")
    if not has_lowercase:
        suggestions.append("Add lowercase letter")
    if not has_number:
        suggestions.append("Add number")
    if not has_symbol:
        suggestions.append("Add symbol")
    if len(password) < 12:
        suggestions.append("Make it at least 12 characters long")
    if not has_no_spaces:
        suggestions.append("Remove spaces")
    if is_common:
        suggestions.append("Avoid common passwords")
    if not suggestions:
        suggestions.append("Your password is strong")
    print("Suggestions:")
    for suggestion in suggestions:
        print("-", suggestion)

    # Stop after displaying all information for a valid password.
    if is_valid:
        print("Password accepted.")
        raise SystemExit

    # Invalid passwords return to the beginning of the loop for another try.
    if not is_valid:
        print("Please try again.\n")
        continue