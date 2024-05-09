//Libreria Math
//Math.PI
//Math.abs(x) valor absoluto
//Math.round(x) redondea
//Math.ceil(x) redondea hacia arriba
//Math.floor(x) redondea hacia abajo
//Math.random() numero aleatorio
//Math.max(x,y,z,...) devuelve el mayor de los numeros
//Math.min(x,y,z,...) devuelve el menor de los numeros
//Math.pow(x,y) devuelve la potencia de x elevado a y
//Math.sqrt(x) devuelve la raiz cuadrada de x
//Math.cbrt(x) devuelve la raiz cubica de x






//intervalos

let contador = 0;
let intervalo = setInterval(function() {
    console.log("Hola");
    contador++;
    if (contador === 3) {
        clearInterval(intervalo);
    }
}, 1000);


//setTimeou


//date

let fecha = new Date();
console.log(fecha);
console.log(fecha.getDate());
console.log(fecha.getDay());
console.log(fecha.getFullYear());
console.log(fecha.getHours());
console.log(fecha.getMinutes());
console.log(fecha.getMonth());
console.log(fecha.getSeconds());
console.log(fecha.getTime());
console.log(fecha.getUTCDate());
console.log(fecha.getUTCDay());
console.log(fecha.getUTCFullYear());
console.log(fecha.getUTCHours());

//formato de fecha
let fecha2 = new Date("2021-02-14");
console.log(fecha2);


//alertas 

alert("Hola");
