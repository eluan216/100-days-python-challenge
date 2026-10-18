import secrets
import string

print("==== PASSWORD GENERATOR ====")
length = int(input("Enter the length of the password: "))
if length < 8:
    print("Password length should be at least 8 characters.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    print(f"Generated Password: {password}")