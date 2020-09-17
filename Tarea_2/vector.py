import numpy as np

class VectorCartesiano:
    '''Es una clase vector cartesiano'''
    def __init__(self, x0=0,y0=0,z0=0):
        
        self.x=x0
        self.y=y0
        self.z=z0
        
        self.magnitude = np.sqrt(self.x**2 + self.y**2 + self.z**2)
        self.data = np.array([self.x, self.y, self.z])
        
    def Print_C(self):
        '''Imprime el vector cartesiano'''
        print(f"[{round(self.x,5)},{round(self.y,5)},{round(self.z,5)}]") 
        
    def __add__(self,other):
        '''Sobrecarga del operador suma en el vector cartesiano'''
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
           
    def __sub__(self,other):        
        '''Sobrecarga del operador resta en el vector cartesiano'''
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __eq__(self, other) :
        '''Sobrecarga del operador == en el vector cartesiano''' 
        return VectorCartesiano(self.x == other.x, self.y == other.y, self.z == other.z)
    
    def __getitem__(self,index) : 
        '''Sobrecarga del  operador [] en el vector cartesiano'''
        print(f"{self.data[index]}") 

    
    def __mul__(self,other):
        '''Sobrecarga del operador multiplicación en el vector cartesiano'''
        return round(self.x*other.x+self.y*other.y+self.z*other.z,5)
        
    
    def Cruz(self,other):
        '''Calcula el producto cruz entre vectores'''
        return VectorCartesiano(self.y*other.z-self.z*other.y , self.z*other.x-self.x*other.z , self.x*other.y-self.y*other.x)

   
    def ToSpherical(self):
        '''Calcula las componentes Esféricas '''
        
        if self.x == 0.0: phi = np.pi/2
        else: phi = np.arctan(self.y/self.x) 
        
        r = np.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = np.arccos(self.z/r) 
           
        return VectorPolar(r,theta,phi)
        


class VectorPolar(VectorCartesiano):
    '''Es una clase vector Polar'''
    def __init__(self, ro=0, th0=0, phi0=0):
        
        self.r=ro
        self.theta=th0
        self.phi=phi0
        self.data = np.array([self.r, self.theta, self.phi])  
           
        
        _x = round(self.r * np.sin(self.theta) * np.cos(self.phi), 5)
        _y = round(self.r * np.sin(self.theta) * np.sin(self.phi),5)
        _z = round(self.r * np.cos(self.theta),5)

        
        VectorCartesiano.__init__(self, _x, _y, _z)
        
    
        if self.r < 0 or self.theta < 0 or self.phi < 0 or self.theta > np.pi or self.phi > 2*np.pi:
            raise ValueError("Los valores de r, theta y phi deben estar dentro de los intervalos:\n r[0,inf]\n theta[0,pi\n phi[0,2*pi)")
    
    def Print_P(self): 
        '''Imprime el vector Polar'''

        print(f"[{round(self.r,5)},{round(self.theta,5)},{round(self.phi,5)}]")