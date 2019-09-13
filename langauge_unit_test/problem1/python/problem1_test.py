import problem1

counter = 0

def testEasy():
    testOutput = problem1.LongestWord("I love dogs")

    if testOutput == "love":
        return 1
    else:
        return 0

def testHard():
    testOutput = problem1.LongestWord("fun&!! time")

    if testOutput == "time":
        return 3
    else:
        return 0

counter = testEasy() + testHard()

print(counter)
