#store hours script

day = input("Enter a day of the week: ").lower()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
    print("Store hours: 9am - 6pm")
elif day == "friday":
    print("Store hours: 9am - 9pm")
elif day == "saturday" or day == "sunday":
    print("Store hours: 10am - 4pm")
else:    print("Invalid day entered. Please enter a valid day of the week.")    