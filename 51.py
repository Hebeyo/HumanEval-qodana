def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([c for c in text if c.lower() not in vowels])

