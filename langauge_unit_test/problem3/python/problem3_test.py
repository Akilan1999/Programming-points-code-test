import problem3

counter = 0

def testEasy():
    testOutput = problem3.FirstReverse("coderbyte")

    if testOutput == "etybredoc":
        return 1
    else:
        return 0

def testHard():
    testOutput = problem3.FirstReverse("I Love Code")

    if testOutput == "edoC evoL I":
        return 3
    else:
        return 0

counter = testEasy() + testHard()

print(counter)