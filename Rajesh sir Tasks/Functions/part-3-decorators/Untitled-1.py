
def upper():
    def decor1(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).upper()
        return wrapper
    return decor1


def doubled():
    def decor2(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * 2
        return wrapper
    return decor2


@upper()
@doubled()
def greet():
    return "Hi Bonkers"


print(greet())