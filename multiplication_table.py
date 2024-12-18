#Prompt user to enter number between(1, 11)
number = int(input("Enter a number to see its multiplication table: "))
# generate a multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number}* {i} = {product}")