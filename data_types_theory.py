##### lecture 1

# input
base = input("give me the base!")
height = int(input("give me the height!"))

# process
area = (int(base) * height) / 2


# output
print(f'The area is: {area}')


##### lecture 2

#  get type of variable
x = 5
print(type(x))

# data types

# Text Type:
#   str, str("Hello World")

# Numeric Types:
#   int, int(20)
#   float, float(20.5)
#   complex (x = 1j), complex(1j)

# Sequence Types:
#   list, ( ["apple", "banana", "cherry"]), list(("apple", "banana", "cherry"))
#   tuple, (("apple", "banana", "cherry")), tuple(("apple", "banana", "cherry"))
#   range, (range(6))

# Mapping Type:
#   dict, {"name" : "John", "age" : 36}, dict(name="John", age=36)

# Set Types:
#   set, {"apple", "banana", "cherry"}, set(("apple", "banana", "cherry"))
#   frozenset, frozenset({"apple", "banana", "cherry"}), frozenset(("apple", "banana", "cherry"))

# Boolean Type:
#   bool,  True or False, bool(5)

# Binary Types:
#   bytes, b"Hello", bytes(5)
#   bytearray, bytearray(5)
#   memoryview, memoryview(bytes(5))

# None Type:
#   NoneType, None

name = 'Alice' * 5
# 'AliceAliceAliceAliceAlice'

# length
print(len(name))


# xor function
