#Python 3.7.6
#-------------------------------------------------------------------
def factorial(n):
    '''Calcula el factorial de un número n:
    Toma un número n y con una variable auxiliar va guardando el resultado 
    de la multiplicación de números sucesivos, desde 1 hasta n. Si lo que ingresa
    no es de tipo entero entonces sale una advertencia.'''
    aux = 1
    if type(n)!=int: print('n debe ser un número entero')
    elif n<0: return 0
    else: 
        for i in range(1,n+1): 
            aux *= i
        return aux

#-------------------------------------------------------------------
def binomial(n,k):
    '''Calcula los coeficientes binomiales:
    Si k es 0 devuleve 1, si k es menor a 1 o alguno de los argumentos ingresados no son 
    enteros devulve una advertencia. Para evitar posibles divisiones por cero, hace un chequeo sobre el 
    el factorial de la resta de n con k'''
    if k==0: return 1
    if factorial(n-k)==0: return 0
    if k<1 or type(k)!=int or type(n)!=int: print('k debe ser un número entero mayor o igual a 1')
    else: return int(factorial(n)/(factorial(k)*factorial(n-k)))

#-------------------------------------------------------------------
def Pascal(n):
    '''Retorna una lista con los resultados del trángulo de Pascal. 
    Cada argumento de la lista es una de las filas del triángulo'''
    p = []
    for k in range(n+1):
        #recorre cada uno de los números hasta llegar al n ingresado (primer argumento de la función Binomial)
        aux = []
        for i in range(n+1):
            #recorre el segundo argumento de la funcón binomial, se detiene si esta es 0
            if binomial(k,i)==0: break
            #agrega a una lista auxiliar cada uno de los resultados de la operación
            aux.append(binomial(k,i))
        #luego de calcular cada uno de resultados de cada fila, agrega esa lista a la lista principal
        p.append(aux)
    return p

#-------------------------------------------------------------------
def draw_pascal(n):
    '''Dibuja el triángulo de Pascal para el número ingresado:
    Toma la función Pascal que devuelve una lista con cada uno de las filas del triángulo.
    Toma la última fila como referencia de centro. Luego une, con un espacio, cada uno de los argumentos de
    de cada fila y los va imprimiendo en un archivo de texto.'''
    
    f = open("Pascal-"+str(n)+".txt", "w")
    f.write('TRIÁNGULO DE PASCAL: \n \n \n')
    last = ' '.join(map(str,Pascal(n)[-1]))
    for i in range(len(Pascal(n))):
        f.write('n=' + str(i) + '    ' + ' '.join(map(str,Pascal(n)[i])).center(len(last)) +'\n')
        print('n=' + str(i) + '    ' + ' '.join(map(str,Pascal(n)[i])).center(len(last)) +'\n')
    f.close()

#-------------------------------------------------------------------
if __name__ == "__main__":
    print("Módulo new_func como script")