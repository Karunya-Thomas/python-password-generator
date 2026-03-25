import string 
password = input("enter your password :")
score = 0

# check length
if len(password) >= 8:
    score += 1

# check uppercase
if any(char.isupper() for char in password):
    score += 1

# check numbers
if any(char.isdigit() for char in password):
    score += 1

# check special characters
if any(char in string.punctuation for char in password):
    score += 1

# strength result

if score == 4:
    print("Strong Password")
elif score == 3:
    print("Medium Password")
else : 
    print("Week Password")