def is_valid_password(password):
    error_messages = []


    if not (6 <= len(password) <= 10):
        error_messages.append("Password must be between 6 and 10 characters")


    if not password.isalnum():
        error_messages.append("Password must consist only of letters and digits")


    if sum(c.isdigit() for c in password) < 2:
        error_messages.append("Password must have at least 2 digits")

    if not error_messages:
        return "Password is valid"
    else:
        return "\n".join(error_messages)


password = input()


result = is_valid_password(password)
print(result)
