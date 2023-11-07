my_name = "Eddie"
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {my_name}")

## If input is not a number this will throw a ValueError
age = int(input("Enter your age: "))
age_in_months = age * 12
print(f"You have lived for {age_in_months} months.")




### test
# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
name = input("Enter your name: ")
print(f"Hello, {name}")

age_in_months = int(input("Enter your age: ")) * 12
print(age_in_months)