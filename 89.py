def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for c in s:
        if c in alphabet:
            result += alphabet[(alphabet.index(c)+2*2) % 26]
        else:
            result += c
    return result
