import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



#------------------------------------------------

class OsciladorAmortiguado:
    
    '''Clase OsciladorAmortiguado. Recibe los argumentos de:
    Condiciones iniciales [posición, momentum], frecuencia de oscilación, amortiguacion, número de iteraciones, tiempo final '''
    
    def __init__(self, condicion_inicial = [0,0], frecuencia = 1, amortiguacion = 0.0, iteraciones=1000, tiempo_final=10 ):
        
        ''' Constructor clase OsciladorAmortiguado '''
        
        self.y0 = condicion_inicial
        self.w = frecuencia
        self.g = amortiguacion
        self.n = iteraciones
        self.tf = tiempo_final
        
        self.t = np.linspace(0, self.tf, self.n)
        
        
        if ((self.g**2)/(self.w**2)) > 1:
            raise ValueError('Underdamped oscillator must be g^2 - w^2 < 0$')
        
    
    def model(self, Y, t, w, g):
    
        y, py = Y[0], Y[1]  #posicion y momentum  
        dYdt = [py, -2*g*py - (w**2)*y]
        
        return dYdt
    
    
    def solution(self, ax, type_graph):
        
        #como es el oscilador amortiguado, se deja constante la frecuencia y se cambia el coheficiente amortiguamiento 
        #Se eligen valores entre el valor iniciado dado y un valor cercano a la frecuencia tal que se cumpla g^2 < w^2 
        G = np.linspace(self.g, self.w*0.8, 6)
        
        for i in range(0,6):

            sol = odeint(self.model, self.y0, self.t, args=(self.w, G[i]))
            
            #dependiendo del tipo de gráfica requerida (de posicion o espacio de fase), elecciona el conjunto de datos a graficar 
            if type_graph =='position': X, Y = self.t, sol[:,0]
            elif type_graph =='phase': X, Y = sol[:,0], sol[:,1]
            else: 
                print('this type of graph is not available')
                break
                
    
            
            ax.plot(X, Y, label= "$\gamma =$"+str(round(G[i], 3)) + "/s")
            ax.legend(loc='upper right', borderaxespad=0.5, borderpad=1)
        

    def graph(self, type_graph):
        
        #se seleccionan el tipo de parametros para la grafica requerida
        if type_graph =='position': 
            title = "Solution of the Oscillator equation"
            Xlabel = "time (s)"
            Ylabel = "$y (m)$"
            fig_size = (25,6)
            
        elif type_graph =='phase': 
            title = "Oscillator's Phase Space "
            Xlabel = "y (m)"
            Ylabel = "$y' (m/s)$"
            fig_size = (10,10)
        
        #else: 
         #   print('this type of graph is not available ') 
          #  pass
        
        fig,ax = plt.subplots( figsize=fig_size)
        plt.rcParams.update({'font.size': 20})
        
        # Se ponen titulo y nombre de los ejes
        ax.set(title = title,
               xlabel = Xlabel,
               ylabel = Ylabel)
        
        #llama al metodo de solucion de acuerdo al tipo de grafica
        self.solution(ax, type_graph)
        plt.show()


#------------------------------------------------

class Oscilador(OsciladorAmortiguado):
    
    '''Clase Oscilador. Clase hija del oscilador Amortiguado.
    Recibe los argumentos de:
    Condiciones iniciales [posición, momentum], frecuencia de oscilación, número de iteraciones, tiempo final.'''
    
    
    def __init__(self, condicion_inicial = [0,0], frecuencia = 1, amortiguacion = 0.0, iteraciones=1000, tiempo_final=10):
        
        OsciladorAmortiguado.__init__(self, condicion_inicial, frecuencia, amortiguacion, iteraciones, tiempo_final)

    def solution(self, ax, type_graph):
        
        #Como es el oscilador armónico cambia la fecuencia hasta unas dos veces la frecuencia ingresada
        W = np.linspace(self.w, self.w*2, 6)
        
        #realiza 5 gráficas 
        for i in range(0,6):
            
            #Resuelve para cada w
            sol = odeint(self.model, self.y0, self.t, args=(W[i], self.g))
            
            #dependiendo del tipo de gráfica requerida (de posicion o espacio de fase), elecciona el conjunto de datos a graficar 
            if type_graph =='position': X, Y = self.t, sol[:,0]
            elif type_graph =='phase': X, Y = sol[:,0], sol[:,1]

            #hace la gráfica con cada w
            ax.plot(X, Y, label= "$\omega =$"+str(round(W[i], 3)) + 'rad/s')
            ax.legend(loc='upper right', borderaxespad=0.5, borderpad=1)

