const PALABRAS = ["hola", "adios", "casa", "perro", "gato", "raton", "elefante", "tigre", "leon", "jirafa", "mono", "pajaro", "pez", "ballena", "delfin", "tiburon", "pulpo", "calamar", "medusa", "estrella", "luna", "sol", "planeta", "satelite", "cometa", "asteroide", "galaxia", "universo", "nebulosa", "supernova", "agujero"];
const INTENTOS = 6;
let palabra, palabraOculta, intentos, letrasUsadas, letrasCorrectas;

function escogerPalabra() {
    return PALABRAS[Math.floor(Math.random() * PALABRAS.length)];
}

function inicializarJuego() {
    palabra = escogerPalabra();
    palabraOculta = "_".repeat(palabra.length).split('').join(' '); // Añadir espacio entre cada letra oculta
    intentos = 0;
    letrasUsadas = [];
    letrasCorrectas = 0;

    actualizarInterfaz();

    // Agregar evento de escucha para la tecla "Enter" en el campo de entrada
    document.getElementById('letra-input').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            let letra = document.getElementById('letra-input').value.toLowerCase();
            document.getElementById('letra-input').value = ""; // Limpiar el campo de entrada después de enviar la letra
            verificarLetra(letra);
        }
    });
}

function actualizarInterfaz() {
    document.getElementById('palabra-oculta').textContent = palabraOculta;
    document.getElementById('intentos-restantes').textContent = INTENTOS - intentos;
    document.getElementById('letras-usadas').textContent = "Letras usadas: " + (letrasUsadas.length > 0 ? letrasUsadas.join(", ") : ''); // Mostrar letras usadas solo si hay alguna
}

function verificarLetra(letra) {
    if (letrasUsadas.includes(letra)) {
        alert("Ya has usado esa letra");
        return;
    }

    letrasUsadas.push(letra);

    if (palabra.includes(letra)) {
        for (let i = 0; i < palabra.length; i++) {
            if (palabra[i] === letra) {
                palabraOculta = palabraOculta.substring(0, i*2) + letra + palabraOculta.substring(i*2 + 1); // Añadir espacio entre cada letra oculta
                letrasCorrectas++;
            }
        }
    } else {
        intentos++;
    }

    if (palabra === palabraOculta.replace(/\s+/g, '')) { // Eliminar espacios para comparar
        document.getElementById('resultado').textContent = "¡Has ganado!";
    }

    if (intentos === INTENTOS) {
        document.getElementById('resultado').textContent = "¡Has perdido! La palabra era: " + palabra;
    }

    actualizarInterfaz();
}

document.getElementById('enviar-letra-btn').addEventListener('click', function() {
    let letra = document.getElementById('letra-input').value.toLowerCase();
    document.getElementById('letra-input').value = ""; // Limpiar el campo de entrada después de enviar la letra
    verificarLetra(letra);
});

inicializarJuego();
