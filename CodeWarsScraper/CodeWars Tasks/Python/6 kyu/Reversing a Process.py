def decode(r):
    key = int(''.join(d for d in r if d.isdigit()))
    letterords = [ord(l.lower()) - 97 for l in r if not l.isdigit()]
    remainders = []
    for i in range(26):
        if (key * i) % 26 <= 25 and (key * i) % 26 not in remainders: remainders.append((key * i) % 26)
        else: return "Impossible to decode"
    decoded = ''.join(chr(remainders.index(c) + 97) for c in letterords if c in remainders)
    return decoded


      