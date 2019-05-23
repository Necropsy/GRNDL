#include <iostream>
#include <math.h>
#include <omp.h>
#include <set>
#include <string>

class GRN {
    private:
        long int NUM_STATES;
        int NUM_NOS;
        std::set<std::string> atratores;
    public:
        //Construtor da classe
        GRN(int aux): NUM_NOS(aux){this->NUM_STATES = (1<<aux);};
        
        std::set<std::string> fullGRN();
        std::set<std::string> atrator(std::string vet);
        void passo(bool * aux);
        void passo(bool * aux, int n);
        bool equals(bool * vet1, bool *vet2, int size);
        void initialState(unsigned long int valor, bool *vet1, bool *vet2, int size);
        std::string boolArraytoString(bool *vet, int size);
        void runGRN(int inicio, int fim, unsigned int * period_vet, unsigned int * transient_vet);
};
