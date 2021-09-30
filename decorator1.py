def d_function(func):
    def inner():
        res = func()
        return res.upper()
    return inner

@d_function
def print_str():
    return "good morning"

print(print_str())