def int_to_mini_roman(number):
    # Write your code here
    roman = ''
    while number > 0:
        if number >= 1000:
            roman += 'm'
            number -= 1000
        elif number >= 900:
            roman += 'cm'
            number -= 900
        elif number >= 500:
            roman += 'd'
            number -= 500
        elif number >= 400:
            roman += 'cd'
            number -= 400
        elif number >= 100:
            roman += 'c'
            number -= 100
        elif number >= 90:
            roman += 'xc'
            number -= 90
        elif number >= 50:
            roman += 'l'
            number -= 50
        elif number >= 40:
            roman += 'xl'
            number -= 40
        elif number >= 10:
            roman += 'x'
            number -= 10
        elif number >= 9:
            roman += 'ix'
            number -= 9
        elif number >= 5:
            roman += 'v'
            number -= 5
        elif number >= 4:
            roman += 'iv'
            number -= 4
        elif number >= 1:
            roman += 'i'
            number -= 1
    return roman

