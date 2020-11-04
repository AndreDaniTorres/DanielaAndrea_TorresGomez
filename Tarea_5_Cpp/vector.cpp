#include <iostream>
using namespace std;
#include "vector.hpp"

class Vector {
    
  private:
    int size;
    int* array; //pointer  

  public: 
    
    Vector(void){
      //constructor por defecto    
        size = 0;
        array = 0;
    }
    
    
    Vector(int size_){ 
      //constructor del vector con tamaño "size" 
        size = size_;
        array = new int[size];
        
        for(int i = 0; i < size; ++i) {
          //construye un array de ceros con el tamaño indicado
            array[i] = 0;   
        }
        
    }
    
    int GetSize() const {  
      //obtiene el tamaño del vector 
        return size;
    }
    
    
    void SetPos(int i, int val) {
      //ingresa en la posicion i, el valor val 
        array[i] = val;
    }
    
    int GetPos(int i) const {
      //obtine el argumento de la posicion i  
      return array[i];
    }
    
    void PrintVec(){
      //imprime cada uno de los argumentos del vector
        cout <<"{";
        for(int i = 0; i < size + 1; ++i) {
            cout << array[i] << ", ";
        }
        cout <<"}"<< endl;
    }
    
    
    int& operator[](int index) {  
      //sobrecarga del operador [] : obtiene el argumento del index
      return array[index];
    }
    
    Vector& operator = (const Vector& v){
      //sobrecarga del operador = : asigna un vector a otro
        
        if (v.size > size){
          //si el tamaño del que se modificará es mayor, lo elimina y vuelve a crear
            delete[] array;
            array = new int[v.size];
        }
        
        //agrega cada una de las entradas del vector nuevo
        for (int i = 0; i < v.size + 1; i++){
            array[i] = v.array[i];
        }
        size = v.size;
        return *this;
    }
    
    Vector operator + (Vector a) {
      //sobrecarga del operador + 
        
        int NewSize = size;
        
        if (a.size > size){
            //crea el vector con el de mayor tamaño
            NewSize = a.size;   
        }
        
        Vector result(NewSize);
        
        for (int i = 0; i < NewSize + 1; ++i){
            if (i < size + 1){
              //suma hasta que los tamaños coinciden
                result.SetPos(i, a.GetPos(i) + this -> GetPos(i));
            }else{
              //simplemente agrega los numeros restantes del vector más grande
                result.SetPos(i, a.GetPos(i));
            }
            
        }
     
        return result;
    }
    
    Vector operator - (Vector a) {
         //sobrecarga del operador -
        int NewSize = size;
        
        if (a.size > size){
            
            NewSize = a.size;   
        }
        
        Vector result(NewSize);
        
        for (int i = 0; i < NewSize + 1; ++i){
            if (i < size + 1){
              //resta hasta que los tamaños coinciden
                result.SetPos(i, this -> GetPos(i) - a.GetPos(i));
            }else{
              //simplemente agrega los numeros restantes del vector más grande
                result.SetPos(i, 0 - a.GetPos(i));
            }
            
        }
     
        return result;
    }
    
};