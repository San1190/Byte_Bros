// Solicitar al usuario que ingrese un número
//let numero = prompt("Introduce un número:");

// Imprimir el número por pantalla si el usuario proporcionó uno
//if (numero !== null) {
    // Convertir el número ingresado a un formato de cadena para asegurarse de que se muestre correctamente
  //  document.write("El número introducido es: " + String(numero));
//}

// lo de arriba es para una terminal en web, en la consola de vscode se hace de la siguiente manera
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Introduce un número: ', (numero) => {
  console.log('El número introducido es: ' + numero);
  rl.close();
});
// en la consola de vscode se hace de esta manera
