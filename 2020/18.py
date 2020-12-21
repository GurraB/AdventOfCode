evaluate = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b
}

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def evaluateExpressionAdditionFirst(expression):
    newExpression = [expression[0]]
    for i in range(1, len(expression), 2):
        if expression[i] == '+':
            newExpression.append(str(evaluate['+'](int(newExpression.pop()), int(expression[i + 1]))))
        else:
            newExpression.append(expression[i])
            newExpression.append(expression[i + 1])
    res = int(newExpression[0])
    for i in range(1, len(newExpression), 2):
        res = evaluate[newExpression[i]](res, int(newExpression[i + 1]))
    return str(res)

def solveLinePart2(line):
    lineArr = list(line.replace(' ', ''))
    expression = []
    for c in lineArr:
        if c == ')':
            parenthesisExpression = []
            while True:
                parenthesisC = expression.pop()
                if parenthesisC == '(':
                    expression.append(evaluateExpressionAdditionFirst(parenthesisExpression[::-1]))
                    break
                else:
                    parenthesisExpression.append(parenthesisC)
        else:
            expression.append(c)
    return evaluateExpressionAdditionFirst(expression)

def evaluateExpressionNoPrecedence(expression):
    res = int(expression[0])
    for i in range(1, len(expression), 2):
        res = evaluate[expression[i]](res, int(expression[i + 1]))
    return str(res)

def solveLinePart1(line):
    lineArr = list(line.replace(' ', ''))
    expression = []
    for c in lineArr:
        if c == ')':
            parenthesisExpression = []
            while True:
                parenthesisC = expression.pop()
                if parenthesisC == '(':
                    expression.append(evaluateExpressionNoPrecedence(parenthesisExpression[::-1]))
                    break
                else:
                    parenthesisExpression.append(parenthesisC)
        else:
            expression.append(c)
    return evaluateExpressionNoPrecedence(expression)

if __name__ == "__main__":
    lines = getInput()
    results = []
    for line in lines:
        results.append(int(solveLinePart1(line)))
    print(sum(results))
    
    results = []
    for line in lines:
        results.append(int(solveLinePart2(line)))
    print(sum(results))
    