def test():
    pass  # pass doesn't do anythng


def testtest(input=3, test=4):
    A = 1
    B = input
    C = test
    return A, B, C


U, V, X = testtest(5)
print(f'the input of U is {U}, of V is {V} and of X {X}')
