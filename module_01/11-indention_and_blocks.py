
# indenting code is a way to make code more readable and maintainable, but in Python it plays a second role, through indentation, the interpreter can determine where a command block starts and where it ends.

# programming languages ​​often use reserved characters or words to determine the beginning and end of a block, but Python uses indentation, adding 4 blank spaces to indicate that a line is within the block

def withdraw(amount):
    if balance >= amount:
        print("amount withdrawn!")
        print("withdraw your money from the ATM")   # inside the def and if structure
    print("thank you for being our customer, have a great day!")    # inside the def structure

balance = 500
withdraw(100)