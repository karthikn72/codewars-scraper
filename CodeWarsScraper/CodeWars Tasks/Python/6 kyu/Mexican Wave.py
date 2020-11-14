def wave(string):
    # Code here
    str2=[]
    for i in range(len(string)):
       if string[i]!=" ":
         str2.append(string[:i]+string[i].upper()+string[i+1:])
    return str2
       