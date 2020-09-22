from vector import *

##Vectores:
a = VectorCartesiano(1.5, 0,  2.4)
b = VectorCartesiano(0,   1,  9)
c = VectorCartesiano(4.2,0.05, 0)

print('Los vectores son: ')
a.Print_C()
b.Print_C()
c.Print_C()

##------------------------
print('En esféricas: ')
a.ToSpherical().Print_P()
b.ToSpherical().Print_P()
c.ToSpherical().Print_P()

##------------------------
print('Producto escalar ')
print('a . b = ',a*b)
print('a . c = ',a*c)
print('b . c = ',b*c)


##------------------------
print('Producto vectorial ')
print('a x b = ', a.Cruz(b).Print_C())
print('a x c = ', a.Cruz(c).Print_C())
print('b x c = ', b.Cruz(c).Print_C())


# a . b = |a||b| cos(theta) ---> theta = arccos(a . b / |a||b|)
##------------------------
print('Ángulo en grados entre ellos: ')

print('a, b = ', np.arccos((a*b)/(a.magnitude*b.magnitude))*(180/np.pi))
print('a, c = ', np.arccos((a*c)/(a.magnitude*c.magnitude))*(180/np.pi))
print('b, c = ', np.arccos((b*c)/(b.magnitude*c.magnitude))*(180/np.pi))


