def main(str1):
    i = 0
    num_equiv = 0
    for i in range(len(str1)):
        if str1[i] == 'I' and i == 0:
            num_equiv += 1
        if str1[i] == 'IV':
            num_equiv += 4
        if str1[i] == 'V':
            num_equiv += 5
        if str1[i] == 'VI':
            num_equiv += 6
        if str1[i] == 'IX':
            num_equiv += 9
        if str1[i] == 'X':
            num_equiv += 10
        if str1[i] == 'XI':
            num_equiv += 11
    
    print(num_equiv)
    '''
    if str1 == 'I':
        num_equiv = 1
    if str1 == 'II':
        num_equiv = 2
    if str1 == 'III':
        num_equiv = 3
    if str1 == 'IV':
        num_equiv = 4
    if str1 == 'V':
        num_equiv = 5
    if str1 == 'VI':
        num_equiv = 6
    if str1 == 'VII':
        num_equiv = 7
    if str1 == 'VIII':
        num_equiv = 8
    if str1 == 'IX':
        num_equiv = 9
    if str1 == 'X':
        num_equiv = 10
    if str1 == 'XI':
        num_equiv = 11
    if str1 == 'XII':
        num_equiv = 12
    if str1 == 'XIII':
        num_equiv = 13
    if str1 == 'XIV':
        num_equiv = 14
    if str1 == 'XV':
        num_equiv = 15
    if str1 == 'XVI':
        num_equiv = 16
    if str1 == 'XVII':
        num_equiv = 17
    if str1 == 'XVIII':
        num_equiv = 18
    if str1 == 'XIX':
        num_equiv = 19
    if str1 == 'XX':
        num_equiv = 20
    if str1 == 'XXI':
        num_equiv = 21
    if str1 == 'XXII':
        num_equiv = 22
    if str1 == 'XXIII':
        num_equiv = 23
    if str1 == 'XXIV':
        num_equiv = 24
    if str1 == 'XXV':
        num_equiv = 25
    if str1 == 'XXVI':
        num_equiv = 26
    if str1 == 'XXVII':
        num_equiv = 27
    if str1 == 'XXVIII':
        num_equiv = 28
    if str1 == 'XXIX':
        num_equiv = 29
    if str1 == 'XXX':
        num_equiv = 30
    
    return num_equiv
    '''

if __name__ == "__main__":
    print(
        main(
            input("Enter Roman numeral: ")
        )
    )