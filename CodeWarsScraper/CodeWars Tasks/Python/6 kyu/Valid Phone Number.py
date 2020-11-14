def validPhoneNumber(phoneNumber):
    print(phoneNumber)
    b=phoneNumber.find("(")
    c=phoneNumber.find(")")
    if b==0 and len(phoneNumber[b:c])==4 and phoneNumber[c+1]==' ' and b!=-1 and c!=-1 and phoneNumber[9]=="-" and len(phoneNumber)==14:
      return True
    return False
    pass