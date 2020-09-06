import funciones as fun

#Funcion Factorial(n) solo puede recibir enteros: 
fun.factorial(5.3)

#Funcion Factorial(n) solo puede entregar enteros.
if type(fun.factorial(5)) == int: print('Función factorial entregra enteros')

#Funcion Binomial(n,k) solo puede recibir enteros: 
fun.binomial(8.9,5.2)

#Funcion Binomial(n,k) solo puede entregar enteros.
if type(fun.binomial(8,5)) == int: print('Función binomial entregra enteros')


#Resultados conocidos para testear que las funciones esten haciendo lo que deben.
if fun.factorial(10) == 3628800 and fun.factorial(15) == 1307674368000: print('Calcula bien los factoriales')

if fun.binomial(10,3) == 120 and fun.binomial(60,50) == 75394027566: print('Calcula bien los coeficientes binomiales')

#Triángulo de Pascal
fun.draw_pascal(9)