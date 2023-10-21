# x = 1
#
# while x <= 10:
#     print(x)
#     x = x+1
#
# print('1) done')


y = 0
total = 0

while y < 10 and total <= 40:
    val = int(input("Plus  "))
    total = total + val

    opt2 = input("do you want to continue to the next one?")
    if opt2 == 'yes':
        continue

    y = y + 1

    opt = input("if you want to quit?")
    if opt == 'yes':
        break
print(f'total is = {total}')
