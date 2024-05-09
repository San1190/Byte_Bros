//arrays en js

//Array literal
let numeros = [1,2,3,4,5];

console.log(numeros[0]);

//Array con constructor
let numeros2 = new Array(1,2,3,4,5);

console.log(numeros2[0]);

//Array con constructor y longitud
let numeros3 = new Array(10);
 
numeros3[0] = 1;

console.log(numeros3[0]);

//Array con constructor y longitud

//Combinar arrays con objetos
let persona = {
    nombre: "Juan",
    edad: 30,
    esEstudiante: true
};

let numeros4 = [1,2,3,4,5,persona];


//combinar 2 arrays
let numeros5 = [1,2,3,4,5];
let numeros6 = [6,7,8,9,10];

let numeros7 = numeros5.concat(numeros6);


//Arreglos asociativos usan nombres en lugar de indices
var person = []; //empty array
person["name"] = "John";
person["age"] = 46;
document.write(person["age"]);
//Metodo