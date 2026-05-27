#gas level indication script
gas_level = int(input("Enter the gas level (0-100): "))
if gas_level >= 75:
    print("Gas level: Full")
elif gas_level >= 50:
    print("Gas level: 3/4")
elif gas_level >= 25:
    print("Gas level: 1/2")
elif gas_level >= 10:
    print("Gas level: 1/4")
else:    print("Gas level: Empty")
