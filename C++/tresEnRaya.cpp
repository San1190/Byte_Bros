// Lo hizo el copiloto a la primera, flipando estoy :)

#include <iostream>
#include <vector>

// Función para imprimir el tablero
void imprimirTablero(const std::vector<std::vector<char>>& tablero) {
    for (const auto& fila : tablero) {
        for (const auto& celda : fila) {
            std::cout << celda << " ";
        }
        std::cout << std::endl;
    }
}

// Función para verificar si hay un ganador
bool hayGanador(const std::vector<std::vector<char>>& tablero, char jugador) {
    // Verificar filas
    for (const auto& fila : tablero) {
        if (fila[0] == jugador && fila[1] == jugador && fila[2] == jugador) {
            return true;
        }
    }

    // Verificar columnas
    for (int i = 0; i < 3; i++) {
        if (tablero[0][i] == jugador && tablero[1][i] == jugador && tablero[2][i] == jugador) {
            return true;
        }
    }

    // Verificar diagonales
    if (tablero[0][0] == jugador && tablero[1][1] == jugador && tablero[2][2] == jugador) {
        return true;
    }
    if (tablero[0][2] == jugador && tablero[1][1] == jugador && tablero[2][0] == jugador) {
        return true;
    }

    return false;
}

int main() {
    std::vector<std::vector<char>> tablero(3, std::vector<char>(3, '-'));

    char jugadorActual = 'X';
    bool juegoTerminado = false;

    while (!juegoTerminado) {
        // Imprimir el tablero
        imprimirTablero(tablero);

        // Obtener la posición del jugador
        int fila, columna;
        std::cout << "Turno del jugador " << jugadorActual << ". Ingrese la fila (0-2): ";
        std::cin >> fila;
        std::cout << "Ingrese la columna (0-2): ";
        std::cin >> columna;

        // Verificar si la posición está disponible
        if (tablero[fila][columna] == '-') {
            // Colocar la ficha del jugador en la posición seleccionada
            tablero[fila][columna] = jugadorActual;

            // Verificar si hay un ganador
            if (hayGanador(tablero, jugadorActual)) {
                std::cout << "¡El jugador " << jugadorActual << " ha ganado!" << std::endl;
                juegoTerminado = true;
            } else {
                // Cambiar al siguiente jugador
                jugadorActual = (jugadorActual == 'X') ? 'O' : 'X';
            }
        } else {
            std::cout << "Posición inválida. Inténtelo de nuevo." << std::endl;
        }
    }

    // Imprimir el tablero final
    imprimirTablero(tablero);

    return 0;
}