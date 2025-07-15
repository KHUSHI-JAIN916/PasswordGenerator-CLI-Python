import random
import string

def generate_password(length):
    if length < 4:
        return "❌ Password length must be at least 4 characters."

    # Ensure inclusion of all character types
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# CLI interface
print("🔐 Password Generator")
try:
    desired_length = int(input("Enter desired password length: "))
    final_password = generate_password(desired_length)
    print(f"\n✅ Generated Password: {final_password}")
except ValueError:
    print("❌ Please enter a valid number.")
