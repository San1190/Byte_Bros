//Introduccion a JS

//Comentarios
//Comentario de una sola linea
/* Comentario de varias lineas */

//Variables
//Declaracion de variables
let x = 5;
let y = 6;
let z = x + y;
console.log(z);

//Tipos de datos
//String
let nombre = "Juan";
console.log(nombre);
//Number
let edad = 30;
console.log(edad);
//Boolean
let esEstudiante = true;
console.log(esEstudiante);

//Operadores
//Aritmeticos
let suma = 5 + 5;
let resta = 10 - 5;
let multiplicacion = 5 * 5;
let division = 10 / 2;
let modulo = 10 % 3;
console.log(suma);
console.log(resta);
console.log(multiplicacion);
console.log(division);
console.log(modulo);

//Comparacion
let a = 5;
let b = 10;
console.log(a == b);
console.log(a != b);
console.log(a > b);
console.log(a < b);
console.log(a >= b);
console.log(a <= b);

//Logicos
let c = 5;
let d = 10;
console.log(c > 3 && d < 20);
console.log(c > 3 || d < 5);
console.log(!(c > 3));

//Condicionales
let hora = 20;

if (hora < 12) {
    console.log("Buenos dias");
} else if (hora < 20) { 
    console.log("Buenas tardes");
} else {
    console.log("Buenas noches");
}

//Ciclos
//For
for (let i = 0; i < 5; i++) {
    console.log(i);
}

//While
let j = 0;
while (j < 5) {
    console.log(j);
    j++;
}

//Funciones
function sumaNumeros(a, b) {
    return a + b;
}

let resultado = sumaNumeros(5, 5);
console.log(resultado);

//Arreglos
let numeros = [1, 2, 3, 4, 5];
console.log(numeros[0]);
console.log(numeros[1]);
console.log(numeros[2]);
console.log(numeros[3]);

//Objetos
let persona = {
    nombre: "Juan",
    edad: 30,
    esEstudiante: true
};

console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.esEstudiante);

//Metodos
let persona2 = {
    nombre: "Juan",
    edad: 30,
    esEstudiante: true,
    saludar: function() {
        console.log("Hola");
    }
};

persona2.saludar();

//Eventos
let boton = document.getElementById("boton");
boton.addEventListener("click", function() {
    console.log("Click");
});

//DOM
let parrafo = document.getElementById("parrafo");
parrafo.innerHTML = "Hola";




//Plantillas literales
let temp = `Hello`;
console.log(temp);


//Metodos de cadena
let cadena = "Hola Mundo";
console.log(cadena.length);
console.log(cadena.indexOf("Mundo"));
console.log(cadena.slice(0, 4));
console.log(cadena.replace("Mundo", "Juan"));
console.log(cadena.toUpperCase());
console.log(cadena.toLowerCase());

