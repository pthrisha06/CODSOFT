import random
import string

print("*** PASSWORD GENERATOR ***")

length = int(input("Enter the desired password length: "))

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

all_characters = uppercase + lowercase + digits + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)

print("\nThank you for using Password Generator!")
