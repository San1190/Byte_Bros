//ECMA  en JS es un estandar que se encarga de definir la especificacion de JS
//
//ECMA 5 es la version de JS que se lanzo en 2009

//ECMA 6 es la version de JS que se lanzo en 2015

//variables y cadenas en ECMA 6
var nombre = "Juan"; //variable global
let edad = 30; //variable local
const PI = 3.1416;

/**var & let

A diferencia de la palabra clave var, que define una variable globalmente, 
o localmente para toda una función sin importar el alcance del bloque, let te permite declarar variables que están limitadas en 
su alcance al bloque, sentencia o expresión en los que se utilizan. */

msg = `Mi nombre es ${nombre} y tengo ${edad} años`; //template string
console.log(msg);


//bucles for in y for of
let numeros = [1,2,3,4,5];
for(let numero of numeros){
    console.log(numero);
}
//for in
for(let i in numeros){
    console.log(i);
}
//diferencia entre for in y for of
//for in devuelve el indice
/*El bucle for...in NO debe usarse para iterar sobre arrays porque, dependiendo del motor de JavaScript, podría iterar en un orden arbitrario. 
Además, la variable de iteración es una cadena, no un número, 
por lo que si intentas hacer alguna matemática con la variable, estarás realizando una concatenación de cadenas en lugar de una suma. */
//for of devuelve el valor


//funciones en ECMA 6
function saludar(){
    console.log("Hola Mundo");
}
saludar();

saludar3() //error



//funciones flecha
const saludar2 = () => console.log("Hola Mundo");

saludar2();

//funcion flecha con parametros
const saludar3 = (nombre) => console.log(`Hola ${nombre}`);

saludar3("Juan");

//funcion flecha con retorno
const sumar = (a,b) => a+b;

console.log(sumar(2,3));


function greet(name = 'usuario') {
    console.log(`Hola, ${name}!`);
}

greet(); // Hola, usuario!
greet('Juan'); // Hola, Juan!


const numbers = [1, 2, 3, 4, 5];

// Utilizando un bucle forEach
numbers.forEach(number => console.log(number));

// Utilizando un bucle for...of
for (const number of numbers) {
    console.log(number);
}



