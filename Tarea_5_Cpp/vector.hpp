//#include <iostream>
//using namespace std;

namespace myvec
{
    class Vector {

        public: 

            Vector(void);

            Vector(int size_);

            int GetSize();
            
            void SetPos(int i, int val);
            
            int GetPos(int i);
            
            void PrintVec();
            
            int& operator[](int index);
            
            Vector& operator = (const Vector& v);
            
            Vector operator + (Vector a);
            
            Vector operator - (Vector a);

        };

};