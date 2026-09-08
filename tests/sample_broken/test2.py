def is_adult(age):
    if age > 18:
        return True
    return False

assert is_adult(18) == True
assert is_adult(17) == False
