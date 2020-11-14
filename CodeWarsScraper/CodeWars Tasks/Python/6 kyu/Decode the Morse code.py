def decodeMorse(morse_code):
    import re
    morse_code=morse_code.strip()
    x = re.split(" {3}",morse_code)
    final=""
    for i in x:
      final+=''.join([MORSE_CODE[letter] for letter in i.split(' ')])+" "
    return final.strip()
