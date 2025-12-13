def my_decorator(function):
    def envelope():
        print('Do something before')
        function()
        print('Do something after')

    return envelope

@my_decorator
def hello_world():
    print('Hello World')

hello_world()
# Do something before
# Hello World
# Do something after