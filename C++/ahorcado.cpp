#include <iostream>
#include <tuple>
#include <vector>
#include <string>
#include <cstdlib> // Para rand()



void show_menu(int intentos, std::string secret_word) {
    std::cout << "Intentos restantes: " << intentos << std::endl;
    std::cout << "Palabra secreta: " << secret_word << std::endl;
    std::cout << "-------------------" << std::endl;
}

std::string generate_secret_word(std::string word) {
    std::string secret_word = "";
    for (int i = 0; i < word.length(); i++) {
        secret_word += "_";
    }
    return secret_word;
}

std::vector<int> is_in(std::string word, char c) {
    std::vector<int> res;
    for (int i = 0; i < word.length(); i++) {
        if (word[i] == c) {
            res.push_back(i);
        }
    }
    return res;
}

int main() {
    int intentos = 7;
    bool game_over = false;
    char letra;
    std::string palabras[] = {"hola", "mundo", "programacion", "computadora", "teclado"};
    int random = rand() % 5;
    std::string palabra = palabras[random];
    std::string secret_word = generate_secret_word(palabra);

    while (!game_over) {
        show_menu(intentos, secret_word);
        
        while (true) {
            std::cout << "Escriba una letra: ";
            std::cin >> letra;
            if (std::cin.fail() || std::cin.peek() != '\n') {
                std::cin.clear();
                std::cin.ignore(100, '\n');
                std::cout << "Error: Debe escribir una sola letra" << std::endl;
            } else {
                break;
            }
        }
        
        std::vector<int> res = is_in(palabra, letra);
        if (res.empty()) {
            intentos--;
        } else {
            for (int i = 0; i < res.size(); i++) {
                secret_word[res[i]] = letra;
            }
        }

        if (intentos == 0) {
            std::cout << "Perdiste! La palabra era: " << palabra << std::endl;
            game_over = true;
        } else if (palabra == secret_word) {
            std::cout << "Ganaste! La palabra era: " << palabra << std::endl;
            game_over = true;
        }
    }

    return 0;
}



