import random

password = ""
pass_length = 8

# lowercase alphabet characters
lower_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# uppercase alphabet characters
upper_alphabet = []
for a in lower_alphabet:
    pass
    upper_alphabet.append(a.upper())

# numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']

# all characters
pass_list = lower_alphabet + upper_alphabet + symbols + numbers

# generating password
for i in range(pass_length):
    password += str(random.choice(pass_list))

print("You generated password is {}".format(password))
