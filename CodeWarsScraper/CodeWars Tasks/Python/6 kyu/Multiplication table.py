def multiplicationTable(size):
    tables=[[] for x in range(size)]
    for i in range(1,size+1):
        for y in range(1,size+1):
            tables[i-1].append(i*y)
    return tables # good luck