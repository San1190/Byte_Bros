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

//for each
numeros.forEach(numero => console.log(numero));



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


//Objetos en ECMA 6 
let persona = {
    nombre: "Juan",
    edad: 30,
    saludar: function(){
        console.log(`Hola soy ${this.nombre}`);
    }
}

persona.saludar();


//Nombres de propiedades calculadas
let nombrePropiedad = "nombre";
let persona2 = {
    [nombrePropiedad]: "Juan",
    ["edad"]: 30,
    saludar(){
        console.log(`Hola soy ${this.nombre}`);
    }
}
//Object.assign() para copiar propiedades de un objeto a otro
let person = {
    name: 'Jack',
    age: 18,
    sex: 'male'
};
let student = {
    name: 'Bob',
    age: 20,
    xp: '2'
};

let newStudent = Object.assign({}, person, student);

console.log(newStudent.name); // Bob
console.log(newStudent.age); // 20
console.log(newStudent.sex); // male
console.log(newStudent.xp); // 2



//entrada generica
function magic(...nums) {
    let sum = 0;
    nums.filter(n => n % 2 == 0).map(el => sum += el);
    return sum;
}
console.log(magic(1, 2, 3, 4, 5, 6));


//el operador spread
let parts = ['shoulders', 'knees'];
let lyrics = ['head', ...parts, 'and', 'toes'];
console.log(lyrics); // ["head", "shoulders", "knees", "and", "toes"]


//clases en ECMA 6
class Persona{
    constructor(nombre, edad){
        this.nombre = nombre;
        this.edad = edad;
    }
    saludar(){
        console.log(`Hola soy ${this.nombre}`);
    }
}

//herencia
class Estudiante extends Persona{
    constructor(nombre, edad, curso){
        super(nombre, edad);
        this.curso = curso;
    }
    saludar(){
        console.log(`Hola soy ${this.nombre} y estudio ${this.curso}`);
    }
}


//Set y Map
let set = new Set();
set.add(5);
set.add(43);
set.add("Hola");
set.add({x: 50, y: 200});
console.log(set.size); //4
console.log(set.has(5)); //true
set.delete(5);
console.log(set.has(5)); //false

let numeros2 = [1,2,3,4,5,6,1,2,3,4,5];
let set2 = new Set(numeros2);
console.log(set2.size); //6


let map = new Map();
map.set("k1", "v1");
map.set("k2", "v2");
console.log(map.get("k1")); //v1
console.log(map.size); //2
map.delete("k1");
console.log(map.get("k1")); //undefined
console.log(map.size); //1

let numeros3 = [[1, "a"], [2, "b"], [3, "c"]];
let map2 = new Map(numeros3);
console.log(map2.size); //3
console.log(map2.get(2)); //b

//Promesas en ECMA 6. Las promesas son objetos que representan la terminación o el fracaso de una operación asíncrona.
let promesa = new Promise((resolve, reject) => {
    let todoCorrecto = true;
    if(todoCorrecto){
        resolve("Todo correcto");
    }else{
        reject("Ha habido un error");
    }
});

promesa.then((mensaje) => {
    console.log(mensaje);
}
).catch((mensaje) => {
    console.log(mensaje);
});


//iteradores y generadores
let iterador = {
    currentValue: 1,
    next(){
        let result = {value: null, done: false};
        if(this.currentValue <= 5){
            result.value = this.currentValue;
            result.done = false;
            this.currentValue++;
        }else{
            result.done = true;
        }
        return result;
    }
}

let item = iterador.next();
while(!item.done){
    console.log(item.value);
    item = iterador.next();
}


//modulos en ECMA 6
//modulo1.js
export const nombre = "Juan";
export const edaad = 30;
export const saludar = () => console.log("Hola Mundo");
// lib/math.js
export let sum = (x, y) => { return x + y; }
export let pi = 3.14;

// app.js
import * as math from "lib/math"
console.log(`2p = + ${math.sum(math.pi, math.pi)}`)


//metodos incorporados en ECMA 6
//Array.prototype.includes()
let numeros4 = [1,2,3,4,5];
console.log(numeros4.includes(3)); //true
console.log(numeros4.includes(6)); //false
