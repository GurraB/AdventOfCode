import re

defaultFieldValidationFunctions = {
    'byr': lambda year: True,
    'iyr': lambda year: True,
    'eyr': lambda year: True,
    'hgt': lambda rawHeight: True,
    'hcl': lambda hairColor: True,
    'ecl': lambda eyeColor: True,
    'pid': lambda passportId: True,
    'cid': lambda countryId: True
}

allowedEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def getInput():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            return lines

def formatPassport(lines):
    fields = [field for line in lines for field in line.split(' ')]
    passport = {}
    for f in fields:
        key, value = f.split(':')
        passport[key] = value
    return passport

def getPassports():
    passports = []
    while True:
        lines = getInput()
        if len(lines) == 0:
            break
        passports.append(formatPassport(lines))
    return passports

def inRange(number, min, max):
    return int(number) >= min and int(number) <= max

def validateHeight(rawHeight):
    if 'cm' in rawHeight:
        return inRange(int(''.join(filter(str.isdigit, rawHeight))), 150, 193)
    elif 'in' in rawHeight:
        return inRange(int(''.join(filter(str.isdigit, rawHeight))), 59, 76)
    else:
        False

def passportIsValid(passport, validationFunctions, *requiredFields, ):
    for f in requiredFields:
        if not f in passport.keys():
            return False
        if not validationFunctions[f](passport[f]):
            return False
    return True

if __name__ == "__main__":
    passports = getPassports()
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fieldValidationFunctions = {
        'byr': lambda year: inRange(year, 1920, 2002),
        'iyr': lambda year: inRange(year, 2010, 2020),
        'eyr': lambda year: inRange(year, 2020, 2030),
        'hgt': lambda rawHeight: validateHeight(rawHeight),
        'hcl': lambda hairColor: True if re.match('^#[0-9a-f]{6}$', hairColor) else False,
        'ecl': lambda eyeColor: eyeColor in allowedEyeColors,
        'pid': lambda passportId: True if re.match('^[0-9]{9}$', passportId) else False,
        'cid': lambda countryId: True
    }
    
    validPassports = 0
    for p in passports:
        if passportIsValid(p, defaultFieldValidationFunctions, *requiredFields):
            validPassports = validPassports + 1
    print(validPassports)

    validPassports = 0
    for p in passports:
        if passportIsValid(p, fieldValidationFunctions, *requiredFields):
            validPassports = validPassports + 1
    print(validPassports)