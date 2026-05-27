
#this is a recipe script
eggs = int(input("Enter the number of eggs you have: "))

flour = 0
for i in range(eggs):
    flour += 2

print(f"You need {flour} cups of flour to make the recipe.")