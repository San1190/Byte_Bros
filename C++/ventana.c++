#include <iostream>
#include <fstream>

// Incluir la librería de SFML para gráficos
// Hay que instalarla con el comando: sudo apt-get install libsfml-dev o manualmente y añadir la ruta al PATH del compilador
#include <SFML/Graphics.hpp>
// Crear una ventana gráfica
using namespace std;

int main() {
    // Crear una ventana gráfica
    sf::RenderWindow ventana(sf::VideoMode(800, 600), "Mi ventana");

    // Bucle principal
    while (ventana.isOpen()) {
        // Procesar eventos
        sf::Event evento;
        while (ventana.pollEvent(evento)) {
            if (evento.type == sf::Event::Closed) {
                ventana.close();
            }
        }

        // Limpiar la ventana
        ventana.clear();

        // Dibujar algo en la ventana
        sf::CircleShape circulo(100);
        circulo.setFillColor(sf::Color::Red);
        ventana.draw(circulo);

        // Mostrar la ventana
        ventana.display();
    }

    return 0;
}

