def rot13(message):
    #your code here
    return ''.join(chr((65 if c.isupper() else 97) + ((ord(c) - (65 if c.isupper() else 97)) + 13)%26) if c.isalpha() else c for c in message)