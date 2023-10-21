# own xor function
# exclusive values

def XOR(val1, val2):
    res = (val1 or val2) and not (val1 and val2)
    return res


print(XOR(True, True)) # False
print(XOR(False, False)) # False
print(XOR(True, False)) # True
print(XOR(False, True)) # True

print( not (5 != 8) and (3.0 >= 3))