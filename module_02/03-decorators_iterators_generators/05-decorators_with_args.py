def my_decorator(function):
    def envelope(*args, **kwargs):
        print('Do something before')
        function(*args, **kwargs)
        print('Do something after')

    return envelope

@my_decorator
def hello_world(nome):
    print(f'Hello World, {nome}')

hello_world('Miguel')