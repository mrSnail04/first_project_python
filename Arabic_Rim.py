romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
def parse_roman(roman):
    result = 0
    try:
        for i, c in enumerate(roman):
            if i+1 < len(roman) and romans[roman[i]] < romans[roman[i+1]]:
                result -= romans[roman[i]]
            else:
                result+=romans[roman[i]]
    except KeyError as ex:
        print('Такой римской цифры не существует:', ex)
    return result

print(parse_roman('I'))
print(parse_roman('II'))
print(parse_roman('IV'))
print(parse_roman('X'))
print(parse_roman('CD'))
print(parse_roman('K'))
