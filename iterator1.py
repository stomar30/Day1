value = 'Sandeep Tomar'
obj = iter(value)

while True:
    try:
        item = next(obj)
        print(item)

    except StopIteration:
        break
    