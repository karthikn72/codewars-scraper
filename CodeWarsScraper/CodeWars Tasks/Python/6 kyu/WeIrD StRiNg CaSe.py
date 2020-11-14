def to_weird_case(string):
    #TODO
    string2=string[0].upper()+string[1:]
    string3=string2.split()
    string4=[]
    for word in string3:
        newword = ""
        i=0
        while i<=len(word)-1:
            try:
                if i/2==int(i/2):
                    newword +=word[i].upper()
                    i+=1
                else:
                    newword += word[i]
                    i+=1
            except IndexError:
                pass
        string4.append(newword)
    return (' '.join(string4))

      