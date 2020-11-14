def find_missing_letter(chars):
      n=0
      while n!=len(chars)-1:
        if chars[n+1]!=chr(ord(chars[n])+1): return chr(ord(chars[n])+1)
        else: n+=1


