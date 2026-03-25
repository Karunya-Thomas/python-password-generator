import string
import random

password = input("Enter your password:")

score = 0
feedback = []

# check length
if len(password) >= 8:
    score += 1

else:
    feedback.append("Use at least 8 characters.")

# check uppercase
if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add uppercase letters")

# check numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add numbers")

# check special characters
if any(char in string.punctuation for char in password):
    score += 1
else:
    feedback.append("Add special characters (!@#$...)")

#Results 
if score == 4:
    print("Strong Password")
elif score == 3:
    print("Medium Password")
else:
    print ("Week Password")

# Suggestions
if feedback:
    print("\nSuggetions to improve:")
    for item in feedback:
        print("-", item)

# Generate password

choice = input("\n Do you want a strong password suggetion? (yes/no):").lower()

if choice == "yes":
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for _ in range(12))
    print("Suggested Strong Password: ",strong_password)
    
