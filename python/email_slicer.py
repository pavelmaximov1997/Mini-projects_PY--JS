email = input("What's your email: ")
index = email.index("@")
username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")