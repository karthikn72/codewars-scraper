def narcissistic( value ):
    numset=[int(str(value)[i])**len(str(value)) for i in range(len(str(value)))]
    return sum(numset)==value
    