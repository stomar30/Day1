class Error(Exception):
    pass

class DivisionByZero(Error):
    pass

try:
    num = int(input("Enter a Number: "))
    
    if num == 0:
        raise DivisionByZero
except DivisionByZero:
    print("Input value is Zero, try again")