def number(lines):
    return ['{0}: {1}'.format(i,lines[i-1]) for i in range(1,len(lines)+1)]