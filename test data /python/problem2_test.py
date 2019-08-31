import problem2


def testCandy():
    candyOutput = problem2.candy()

    if candyOutput == "candy1":
        return 1
    else:
        return 0

counter = testCandy()

print(counter)
