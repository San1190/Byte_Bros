#include <iostream>

class  Laberinto{
    public:
        Laberinto();
        void mostrar();
        void mover(char);
        bool termino();
    private:
        char laberinto[5][5];
        int x, y;

        void inicializar();


    void inicializar(){
        for (int i = 0; i < 5; i++){
            for (int j = 0; j < 5; j++){
                laberinto[i][j] = ' ';
            }
        }
        x = 0;
        y = 0;
        laberinto[x][y] = 'X';
        laberinto[4][4] = 'F';
    }

    void mostrar() {
        for (int i = 0; i < 5; i++){
            for (int j = 0; j < 5; j++){
                std::cout << laberinto[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
};   