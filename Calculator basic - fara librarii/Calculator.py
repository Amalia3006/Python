
def findRoundParenthesis(testString):
    if testString.find("(") != -1 and testString.find(")") != -1:
        return (testString.find("("), testString.find(")"))
    elif testString.find("(") != -1 or testString.find(")") != -1:
        return 0  # "Structura incorecta"
    else:
        return 1  # "NU Exista paranteze Rotunde"


def difineNumbers(testString, a, b):
    try:
        newNumber = int(testString[a:b])
        return newNumber
    except:
        return "expresie invalida"


def schimbareIndexi(listOfNumbers, listOfOperationPosition, index, rezultat):
    listOfOperationPosition.remove(listOfOperationPosition[index])
    listOfNumbers.insert(index-1, rezultat)
    listOfNumbers.remove(listOfNumbers[index])
    listOfNumbers.remove(listOfNumbers[index])


def operatiiDeGrad1(listOfNumbers, listOfOperationPosition, index, operatie):
    if operatie == "*":
        rezultat = listOfNumbers[index-1]*listOfNumbers[index]
    else:
        rezultat = listOfNumbers[index-1]/listOfNumbers[index]
    schimbareIndexi(listOfNumbers, listOfOperationPosition, index, rezultat)


def operatiiDeGrad2(listOfNumbers, listOfOperationPosition, index, operatie):
    if operatie == "+":
        rezultat = listOfNumbers[index-1]+listOfNumbers[index]
    else:
        rezultat = listOfNumbers[index-1]-listOfNumbers[index]
    schimbareIndexi(listOfNumbers, listOfOperationPosition, index, rezultat)


def returningCalcul(listOfNumbers, listOfOperationPosition):
    i = 0
    while i < len(listOfOperationPosition):
        if listOfOperationPosition[i][1] in ["*", "/"]:
            operatiiDeGrad1(listOfNumbers, listOfOperationPosition,
                            i, listOfOperationPosition[i][1])
        else:
            i += 1
    i = 0
    while i < len(listOfOperationPosition):
        if listOfOperationPosition[i][1] in ["+", "-"]:
            operatiiDeGrad2(listOfNumbers, listOfOperationPosition,
                            i, listOfOperationPosition[i][1])
        else:
            i = i+1
    print(listOfOperationPosition)
    print(listOfNumbers)
    if listOfOperationPosition[1][1] == "=":
        return listOfNumbers[0]


def calculMatematic(testString):
    listOfNumbers = []
    listOfOperationPosition = []
    for i in range(len(testString)):
        if testString[i] in ["+", "-", "/", "*", "="]:
            listOfOperationPosition.append((int(i), testString[i]))
    listOfOperationPosition.insert(0, (-1, None))

    for i in range(0, len(listOfOperationPosition)-1):
        listOfNumbers.append(difineNumbers(
            testString, int(listOfOperationPosition[i][0]+1), int(listOfOperationPosition[i+1][0])))

    return returningCalcul(listOfNumbers, listOfOperationPosition)


def CalculatorPython():
    stringToSolve = str(input("Introduceti calculul:"))
    while findRoundParenthesis(stringToSolve) == 0 or stringToSolve[len(stringToSolve)-1] != "=":
        stringToSolve = str(input("Introduceti calculul:"))

    return calculMatematic(stringToSolve)


print(CalculatorPython())
