def tickets(people):
    change = n25 = n50 = n100 = 0
    enough = "YES"
    for x in people:
        required = x - 25
        if x == 25:
            change += 25
            n25 += 1
        elif x == 50:
            change += 50
            n50 +=1
        elif x == 100:
            change += 100
            n100 += 100
        if change >= required:
            if required == 25 and n25 >= 1:
                n25 -= 1
                change -= 25
            elif required == 75 and n25 >=1 and n50 >=1:
                n25 -= 1
                n50 -= 1
                change -= 75
            elif required == 75 and n25 >=3:
                n25 -= 3
                change -= 75
            elif x == 25:
                pass
            else:
                enough = "NO"
        else:
            enough = "NO"
    return enough
