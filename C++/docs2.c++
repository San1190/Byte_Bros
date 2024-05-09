#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <vector>
#include <map> 
#include <stdexcept>

using namespace std;

// Definición de una clase Persona
class Persona {
private:
    string nombre;
    int edad;
public:
    // Constructor
    Persona(string _nombre, int _edad) : nombre(_nombre), edad(_edad) {}

    // Métodos para obtener y establecer nombre y edad
    string getNombre() { return nombre; }
    int getEdad() { return edad; }
    void setNombre(string _nombre) { nombre = _nombre; }
    void setEdad(int _edad) { edad = _edad; }

    // Método para mostrar información de la persona
    void mostrarInfo() {
        cout << "Nombre: " << nombre << ", Edad: " << edad << endl;
    }
};

// Función para manejar excepciones
void dividir(int a, int b) {
    if (b == 0) {
        throw invalid_argument("División por cero no permitida");
    }
    cout << "Resultado de la división: " << a / b << endl;
}

// Plantilla de función para encontrar el elemento más grande en un vector
template<typename T>
T encontrarMaximo(vector<T> vec) {
    T maximo = vec[0];
    for (const T& elemento : vec) {
        if (elemento > maximo) {
            maximo = elemento;
        }
    }
    return maximo;
}

int main() {
    // Manejo de archivos
    ofstream archivoSalida("datos.txt");
    archivoSalida << "Hola, mundo!" << endl;
    archivoSalida.close();

    ifstream archivoEntrada("datos.txt");
    string linea;
    while (getline(archivoEntrada, linea)) {
        cout << "Línea leída del archivo: " << linea << endl;
    }
    archivoEntrada.close();

    // Expresiones regulares
    string texto = "La fecha de hoy es 2024-05-09";
    regex patron("\\d{4}-\\d{2}-\\d{2}");
    smatch coincidencias;
    if (regex_search(texto, coincidencias, patron)) {
        cout << "Fecha encontrada en el texto: " << coincidencias[0] << endl;
    }

    // Programación orientada a objetos
    Persona persona("Juan", 30);
    persona.mostrarInfo();

    // Gestión de excepciones
    try {
        dividir(10, 2);
        dividir(10, 0); // Esto lanzará una excepción
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }

    // Plantillas y bibliotecas STL adicionales
    vector<int> numeros = {1, 5, 3, 7, 2};
    cout << "El número máximo en el vector es: " << encontrarMaximo(numeros) << endl;

    map<string, int> edadPersonas;
    edadPersonas["Juan"] = 30;
    edadPersonas["María"] = 25;
    cout << "Edad de Juan: " << edadPersonas["Juan"] << endl;

    return 0;
}
