def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def getGroups():
    groups = []
    while True:
        lines = getInput()
        if len(lines) == 0:
            break
        groups.append(lines)
    return groups

def flattenGroup(group):
    return [question for person in group for question in person]

def getUniqueQuestions(group):
    return set(flattenGroup(group))

def getQuestionsEveryoneAnsweredYesTo(group):
    commonQuestionsInGroup = set(group[0])
    for personQuestionnaire in group:
        commonQuestionsInGroup = commonQuestionsInGroup.intersection(personQuestionnaire)
    return commonQuestionsInGroup

if __name__ == "__main__":
    groups = getGroups()
    sumOfQuestions = 0
    for g in groups:
        sumOfQuestions = sumOfQuestions + len(getUniqueQuestions(g))
    print(sumOfQuestions)

    sumOfQuestions = 0
    for g in groups:
        sumOfQuestions = sumOfQuestions + len(getQuestionsEveryoneAnsweredYesTo(g))
    print(sumOfQuestions)