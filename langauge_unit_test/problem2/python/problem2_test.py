import problem2

counter = 0

def testEasy():
    testOutput = problem2.FirstFactorial(4)

    if testOutput == 24:
        return 1
    else:
        return 0

def testHard():
    testOutput = problem2.FirstFactorial(8)

    if testOutput == 40320:
        return 3
    else:
        return 0

counter = testEasy() + testHard()

print(counter)
