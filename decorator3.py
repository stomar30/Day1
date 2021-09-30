def upper_d(func):
    def inner():
        res = func()
        return res.upper()
    return inner

def split_d(func):
    def wrapper():
        str1 = func()
        return str1.split()
    return wrapper
    
@split_d
@upper_d
def print_str():
    return "good morning"

print(print_str())