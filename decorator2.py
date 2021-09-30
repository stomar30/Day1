def div_decorator(func):
    def inner(a,b):
        if b == 0:
            return "Pls enter a valid number"
        return func(a,b)
    return inner

@div_decorator
def div(a,b):
    return a/b

print(div(4,0))
print(div(6,7))