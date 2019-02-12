# print("Enter your name ", end="")
name = input("Enter your name ")
age = int(input("Your age "))
# print("Hello ", name, ".", sep='')
print(f"Hello, {name}.")

# my new line
if age < 10:
    print("Hi")
elif 10 <= age <=30:
    print("Hello")
else:
    print("Good day")

while (True):
    break