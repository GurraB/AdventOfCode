def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def getAllInput():
    data = {'ticketFields': [], 'myTicket': [], 'nearbyTickets': []}
    data['ticketFields'] = getInput()
    data['myTicket'] = getInput()[1:]
    data['nearbyTickets'] = getInput()[1:]
    return data

def parseTicketFields(ticketFields):
    ticketRules = {}
    for field in ticketFields:
        fieldNameAndRanges = field.split(':')
        fieldName = fieldNameAndRanges[0]
        ranges = fieldNameAndRanges[1]
        parts = ranges.split()
        range1 = [int(n) for n in parts[0].split('-')]
        range2 = [int(n) for n in parts[2].split('-')]
        ticketRules[fieldName] = ((range1[0], range1[1]), (range2[0], range2[1]))
    return ticketRules

def parseTicket(ticketString: str):
    return [int(n) for n in ticketString.split(',')]

def isWithinRange(value, range):
    return range[0] <= value and value <= range[1]

def getApplicableFieldsForValue(value, ticketRules):
    applicableFields = []
    for rule in ticketRules.keys():
        (range1, range2) = ticketRules[rule]
        if isWithinRange(value, range1) or isWithinRange(value, range2):
            applicableFields.append(rule)
    return applicableFields

def getInvalidFieldsInTicket(ticket, ticketRules):
    fieldIndices = []
    for i in range(len(ticket)):
        if len(getApplicableFieldsForValue(ticket[i], ticketRules)) == 0:
            fieldIndices.append(i)
    return fieldIndices

if __name__ == "__main__":
    data = getAllInput()
    ticketRules = parseTicketFields(data['ticketFields'])
    myTicket = parseTicket(data['myTicket'][0])
    nearbyTickets = [parseTicket(t) for t in data['nearbyTickets']]
    scanningErrorRate = 0
    for nearbyTicket in nearbyTickets:
        invalidIndices = getInvalidFieldsInTicket(nearbyTicket, ticketRules)
        scanningErrorRate += sum([nearbyTicket[i] for i in invalidIndices])
    print(scanningErrorRate)

    # -------------------------------part 2--------------------------------

    validTickets = []
    for nearbyTicket in nearbyTickets:
        if len(getInvalidFieldsInTicket(nearbyTicket, ticketRules)) == 0:
            validTickets.append(nearbyTicket)
    
    fieldsForIndex = [(i, set(ticketRules.keys())) for i in range(len(myTicket))]
    for ticket in validTickets:
        for i in range(len(ticket)):
            applicableFieldsForIndex = getApplicableFieldsForValue(ticket[i], ticketRules)
            fieldsForIndex[i] = (fieldsForIndex[i][0], fieldsForIndex[i][1].intersection(set(applicableFieldsForIndex)))
    
    removed = True
    while removed:
        removed = False
        for i in range(len(fieldsForIndex)):
            if len(fieldsForIndex[i][1]) == 1:
                toRemove = list(fieldsForIndex[i][1])[0]
                for j in range(len(fieldsForIndex)):
                    if i == j:
                        continue
                    if toRemove in fieldsForIndex[j][1]:
                         fieldsForIndex[j][1].remove(toRemove)
                         removed = True

    departureFields = [f for f in fieldsForIndex if 'departure' in list(f[1])[0]]

    departureProduct = 1
    for departureField in departureFields:
        (i, _) = departureField
        departureProduct *= myTicket[i]
    print(departureProduct)