import random

def RandomNumberInFile(countOfNumber):
    file = open("what.txt", "w")

    numberInLine = 0

    for i in range(countOfNumber):
        if (numberInLine >= 10):
            file.write("\n")
            numberInLine = 0

        file.write(str(random.randint(0, 100)) + " ")
        numberInLine += 1

    file.write("\n")
    file.close()


def SquareOfNumberInFile(countOfLine):
    file = open("what.txt", "r+")
    lines = file.readlines()
    cursPos = 0
    for line in lines:
        numbers = line.split()
        cursPos += len(line)
        for n in numbers:
            file.seek(0, 2)
            file.write(str(int(n) ** 2) + " ")
        file.write("\n")
        file.seek(cursPos)
    file.seek(0, 2)
    file.close()

RandomNumberInFile(1000)
SquareOfNumberInFile(100)