import funciones as fun

def probability(n, k, more=False):
    '''Por defecto calcula la probabilidad de que al lanzar una moneda n veces,
    resulte un numero k de veces cara (sello).
    more = mayor que k'''
    prob = 0
    var = ''
    if more == True: 
        var='más de'
        for i in range(k,n): #experimento n veces, caiga k veces
            prob += (fun.binomial(n,i))/(2**n)
    else: 
        prob = (fun.binomial(n,k))/(2**n)
        
    print(f"la probabilidad de que si se hace lanza una moneda {n:.0f} veces, el resultado sea {var} {k} veces cara es de aproximadamente: {round(prob*100,4)}%")
    
    
probability(100,10)
probability(100,30)
probability(100,30, True)