
# it's possible to define functions within other functions; these functions are called internal functions

def main():
    print('This is the main() function')

    def inner_function():
        print('This is the inner function!')

    def inner_function2():
        print('This is the second inner function!!')

    inner_function()
    inner_function2()

main()
# This is the main() function
# This is the inner function!
# This is the second inner function!!