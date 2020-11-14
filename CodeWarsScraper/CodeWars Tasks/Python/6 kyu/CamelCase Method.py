def camel_case(string):
    #your code here
    string=string.split()
    for i in range(len(string)):
      string[i]=string[i].capitalize()
    return ''.join(string)
    