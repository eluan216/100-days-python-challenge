def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    return strength

    print("\n===== PASSWORD REPORT =====")
    print(f"Password length: {len(password)} characters")
    print(f"Password strength: {check_password(password)}")

    if len(password) < 8:
        print("Recommendation: Use at least 8 characters.")
    if not any(char.isupper() for char in password):
        print("Recommendation: Include at least one uppercase letter.")
    if not any(char.islower() for char in password):
        print("Recommendation: Include at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        print("Recommendation: Include at least one digit.")
    if not any(not char.isalnum() for char in password):
        print("Recommendation: Include at least one special character.")

print("🔐 PASSWORD STRENGTH CHECKER")

password = input("Enter your password to check its strength: ")
check_password(password)