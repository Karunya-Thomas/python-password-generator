import random
import string
print("Password Generator!")

len = int(input("Enter the lenghth of the password: "))

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
numbers  = "0123456789"
punctiation = "!@#$%^&*()"

characters = alpha + numbers + punctiation
password = ""

for i in range (len):
    password +=random.choice(characters)

print("Generated password:", password)