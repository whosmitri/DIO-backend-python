
# "*args" and "**kwargs" are special syntaxes that allow a function to accept a variable number of arguments. "*args" collects positional arguments in a tuple, while "**kwargs" collects named arguments (or keyword arguments) in a dictionary.

def display_poem(full_date, *args, **kwargs):
    text = "\n".join(args)
    metadata = "\n".join([f"{key.title()}: {value}" for key, value in kwargs.items()])
    message = f"{full_date}\n\n{text}\n\n{metadata}"
    print(message)

display_poem(
    'Sunday, November 9th, 2025',

    'Soneto da Fidelidade \n',
    
    'De tudo, ao meu amor serei atento',
    'Antes, e com tal zelo, e sempre, e tanto',
    'Que mesmo em face do maior encanto',
    'Dele se encante mais meu pensamento.\n',

    'Quero vivê-lo em cada vão momento',
    'E em louvor hei de espalhar meu canto',
    'E rir meu riso e derramar meu pranto',
    'Ao seu pesar ou seu contentamento.\n',

    'E assim, quando mais tarde me procure',
    'Quem sabe a morte, angústia de quem vive',
    'Quem sabe a solidão, fim de quem ama\n',

    'Eu possa me dizer do amor (que tive):',
    'Que não seja imortal, posto que é chama',
    'Mas que seja infinito enquanto dure.',

    author='Vinicius de Moraes',
    year=1939
)