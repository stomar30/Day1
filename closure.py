def outer():
    x = 6

    def inner():
        print(x)

    return inner

a = outer()

a()