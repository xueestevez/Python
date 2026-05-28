#this is a set of functions
def user_info(x, y, age):
    return f"Your name is {x} {y} and you are {age} years old."
x = input("Enter your first name: ")
y = input("Enter your last name: ")
z = int(input("Enter your age: "))
print(user_info(x, y, z))
