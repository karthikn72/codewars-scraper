def alphabet_position(text):
    new=""
    text=text.lower()
    for i in text:
      if ord(i)-ord('a')<=26 and ord(i)-ord('a')>=0: new+=str(ord(i)-ord('a')+1)+" "
    return new.strip()