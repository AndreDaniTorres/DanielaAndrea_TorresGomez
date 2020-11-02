import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

##-----------------------------------

class FinitWell:
    
    def __init__(self, potential_function = lambda z: z, potential_energy = 6):
    
        ''' Constructor clase del pozo finito de potencial '''
        self.hbar = 1
        self.m = 1 
        self.a = 3         #Tamaño del pozo
        self.N = 6561      #Numero de puntos de la cuadrícula (como es un grid, el numero de puntos debe ser una potencia del tamaño del pozo)
        self.b = 200       #Límites espaciales donde se evalua el problema 

        self.V_Potential = potential_function
        self.Vo = potential_energy

      
        self.z = np.linspace(-self.b/2.,self.b/2.,self.N)
        self.dz = self.z[1]-self.z[0]            


    def Fill_V(self, Vo):
    
        '''Llena el array de la barrera de potencial de acuerdo a los límites establecidos'''

        V=np.zeros(self.N)
        
        for i in range(self.N):
            if self.z[i]< -self.a/2. or self.z[i]> self.a/2.: 
                V[i]= self.V_Potential(self.Vo)
        return V

    def Hamiltonian(self):

        '''Encuentra el Hamiltoniano del problema en su forma matricial'''

        T = 1./(self.dz**2)*(np.diag(np.ones(self.N-1),-1) -2* np.diag(np.ones(self.N),0) + np.diag(np.ones(self.N-1),1))
        H = -(self.hbar**2)/(2.0*self.m)*T + np.diag(self.Fill_V(self.Vo)) 
        return H

    def Eingenfunction(self):

        '''Encuentra los autovalores y autofunciones del Hamiltoniano, que corresponden a las Energías y los autoestados'''

        E,tran_psi = np.linalg.eigh(self.Hamiltonian())
        psi = np.transpose(tran_psi)
        return E, psi

    def graph(self, y):

        '''Parámetros para las gráficas'''

        plt.figure(figsize=(12,10))
        plt.xlim((-self.a/2 - 2, self.a/2 + 2))  #para poder visualizar las funciones
        plt.axvline(x=-self.a/2, color='black')                 #límites del pozo
        plt.axvline(x=self.a/2, color='black')
        plt.xlabel('z', size=17)
        plt.ylabel(y,size=17)

        E, psi = self.Eingenfunction()
        plotting = np.array([psi[i] for i in range(5) if E[i]<self.Vo])

        return plotting, E, psi

    def eingen_graph(self):
        
        '''Hace la gráfica de los primeros 4 autoestados del Hamiltoniano. Cuando la Energía es menor que la del potencial dado'''

        plotting, E, psi = self.graph('$\psi(z)$')

        for i in range(4):
            plt.plot(self.z, plotting[i]/np.sqrt(self.dz), label = f"E = {E[i]/E[0]:.2f} Eo", linewidth=2)

        plt.legend()
  
    def density_graph(self):

        '''Hace la gráfica de las primeras 4 densidades de probabilidad'''

        plotting, E, psi = self.graph('$|\psi (z)|^2$')
        density = plotting**2
    
        for i in range(4):
            plt.plot(self.z, density[i]/np.sqrt(self.dz)**2, label = f"E = {E[i]/E[0]:.2f} Eo", linewidth=2)
    
        plt.title('Densidad de probabilidad')
        plt.legend()
        
    def time_dependent(self):
    
        E, psi = self.Eingenfunction()
    
        t = np.linspace(0, 8, 4)
        self.graph('$|\psi (z)|^2$')

        for i in range(len(t)):
            superpos = np.zeros(len(psi[0]))  #toma un tiempo determinado 
            for j in range(4):                #principio de superposición con 4 autoestados
                superpos += psi[j]*np.cos(-t[i]*E[j]/(self.hbar*E[0]))
            plt.plot(self.z, superpos**2, label=f"t = {t[i]:.2f}")
            plt.legend()

##-----------------------------------------

class InfinitWell(FinitWell):
    
    def __init__(self, potential_function = lambda z: z, potential_energy = 0):
        FinitWell.__init__(self, potential_function, potential_energy)

    def graph(self, y):

        '''Parámetros para las gráficas'''

        plt.figure(figsize=(10,7))
        plt.title('Evolución temporal - Principio de Superposición')
        plt.xlabel('z', size=14)
        plt.ylabel(y,size=14)

        E, psi = self.Eingenfunction()
        plotting = np.array([psi[i] for i in range(5)])
    
        return plotting, E, psi

    def time_dependent(self):
    
        E, psi = self.Eingenfunction()
    
        t = np.linspace(0, 8, 4)
        self.graph('$|\psi (z)|^2$')

        for i in range(len(t)):
            superpos = np.zeros(len(psi[0]))  #toma un tiempo determinado 
            for j in range(4):                #principio de superposición con 4 autoestados
                superpos += psi[j]*np.cos(-t[i]*E[j]/(self.hbar*E[0]))
            plt.plot(self.z, superpos**2, label=f"t = {t[i]:.2f}")
            plt.legend()



##--------------------------

particle = FinitWell()
particle.eingen_graph()
particle.density_graph()
particle.time_dependent()

##--------------------------

particula2 = InfinitWell()
particula2.eingen_graph()
particula2.density_graph()
particula2.time_dependent()