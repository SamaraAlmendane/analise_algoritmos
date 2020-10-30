def num_int(n):
    count = 0
       
    #for não finalizado
    '''for n in range(n):
        if n % 2 == 0:
            n = (n/2)
            count += 1
            #return  n + 1
        else:
            n = (3*n)+1
            count += 1            
            #return n + 1
    else:
        result = n + count'''

    while n != 1:
        if n % 2 == 0:
            n = (n/2)
            count += 1
            #return  n + 1
        else:
            n = ((2*n)-2)
            count += 1
            #return n + 1
        
    result = n + count
        
    
    return result

'''def soma(n):
    count = 0

    n = 3*n
    count += 1
    result = n + count
    return result'''

print(num_int(3))