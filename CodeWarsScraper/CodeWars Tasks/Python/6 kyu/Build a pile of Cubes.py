def find_nb(m):
    # your code
    vol=vol2=m
    count=n=i=0
    while count<=vol:
        i+=1
        count+=i**3
    if (count-(i**3))==vol:
        return(i-1)
    else:
        return -1
        