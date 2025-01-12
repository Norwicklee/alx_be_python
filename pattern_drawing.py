#Prompt user to enter a positive integer
size = int(input("Enter the size of the pattern: "))
# initialize a counter and use while loop to iterate through each row
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
#increament the row counter
    row += 1



