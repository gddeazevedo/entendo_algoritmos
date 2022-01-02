def greet_2(name: str):
    print(f'How are you, {name}?')


def bye():
    print('Ok, bye!')


def greet(name: str):
    print(f'Hello, {name}!')
    greet_2(name)
    print('Getting ready to say bye...')
    bye()
