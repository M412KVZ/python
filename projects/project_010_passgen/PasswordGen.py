import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
length = int(input("[*] Input Password Length: "))
while len(password) != length:
    password = password + random.choice(chars)
    if len(password) == length:
        print("Password: %s" % password)