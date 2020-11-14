import string
from codecs import encode as _dont_use_this_

def rot13(message):
    lower=[chr(i+97) for i in range(26)]
    upper=[chr(i+65) for i in range(26)]
    newstring=""
    for i in message:
      if i in lower and ord(i)+13<=122:
        newstring+=chr(ord(i)+13)
      elif i in lower and ord(i)+13>122:
        newstring+=chr(96+((ord(i)+13)-122))
      elif i in upper and ord(i)+13<=90:
        newstring+=chr(ord(i)+13)
      elif i in upper and ord(i)+13>90:
        newstring+=chr(64+((ord(i)+13)-90))
      else:
        newstring+=str(i)
    return newstring

