
# loop structures are used to repeat a piece of code a certain number of times, this number can be known previously or determined through a logical expression

print("### FOR ###")
# the "for" loop is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects, it executes a block of code once for each item in the sequence

print("#### EXAMPLES ####")

print("##### ONE #####")

text = input("Enter a text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")
else:
    print()
    print("end of for loop")

print("##### TWO #####")

# range function: a Python's built-in function
#   3 args: start (optional), stop (required), step (optional)
for i in range(5):  # generates numbers from 0 to 4
    print(i, end=" ")

print()

for i in range(1, 6):   # generates numbers from 1 to 5
    print(i)

print("### WHILE ###")
# used to repeat a block of code multiple times, usually used when we don't know the exact number of times the block of code should be executed

print("#### EXAMPLES ####")

print("##### ONE #####")

option = -1

while (option != 0):
    option = int(input("[1] Withdraw \n[2] Statement \n[0] Exit \n"))

    if (option == 1):
        print("Withdrawing...")
    elif (option == 2):
        print("Displaying statement...")
    else:
        print("Please enter a valid option.")

print("##### TWO #####")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("##### TWO #####")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)