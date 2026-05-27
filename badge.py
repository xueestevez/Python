#this is a script for a security badge access system


badge_id = input("Enter your badge ID: ")
if badge_id == "12345":
    print("Access granted. Welcome, employee!")
elif badge_id == "67890":
    print("Access granted. Welcome, manager!")
else:    print("Access denied. Invalid badge ID.")  