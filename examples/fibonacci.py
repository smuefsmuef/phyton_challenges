def calculate_fibonacci():
    number_of_items = -1

    while number_of_items < 0:
        number_of_items = int(input("how many items should your fibonacci list contain?"))

    # calculate list,  (a, b) => b, a + b, and then append
    fibonacci = [0, 1]  # a, b

    if number_of_items != 0:
        while len(fibonacci) < number_of_items:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci
    else:
        return []


result = calculate_fibonacci()

print(f'result + {result}')
