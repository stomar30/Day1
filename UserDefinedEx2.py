class UserError(RuntimeError):
    def __init__(self, s):
        self.value = s

try:
    raise UserError("User defined error")

except UserError as e:
    print(e.value)