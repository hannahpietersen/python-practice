print("Create accoutn now")
username = input("Enter the username: ")
password = input("Enter the password: ")

print("Your account has been created successfully")
print('Login now')

username2 = input("Enter the username: ")
password2 = input("Enter the password: ")

if username == username2 and password == password2:
    print("Login successful")
else:
    print("Invalid credentials")
