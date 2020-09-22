from MasaResorte import *

osDamp = OsciladorAmortiguado(condicion_inicial = [10,0], frecuencia = 1, amortiguacion = 0.2, iteraciones=1000, tiempo_final=20)

osDamp.graph('position')
osDamp.graph('phase')

#------------------------------

os = Oscilador(condicion_inicial = [10,0], frecuencia = 1,iteraciones=1000, tiempo_final=20)

os.graph('position')
os.graph('phase')