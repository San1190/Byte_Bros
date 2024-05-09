// Descripcion detalla de el funcionamiento de los objetos en JS
//
// //Objetos

//Objeto literal
let persona = {
    nombre: "Juan",
    apellido: "Perez",
    edad: 30,
    direccion: {
        calle: "Av. Siempre viva",
        numero: 123
    }
};

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.direccion.calle);

//otro metodo se puede acceder tambien a los valores de los objetos con la notacion de corchetes
console.log(persona["nombre"]);
console.log(persona["apellido"]);
console.log(persona["edad"]);


//Objeto con constructor
function Persona(nombre, apellido, edad) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
}

let persona1 = new Persona("Juan", "Perez", 30); //el new es para crear un nuevo objeto
let persona2 = new Persona("Maria", "Lopez", 25); //el new es para crear un nuevo objeto


console.log(persona1.nombre);
console.log(persona1.apellido);


console.log(persona2.nombre); //buenos dias