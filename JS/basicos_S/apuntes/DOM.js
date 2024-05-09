// resumen sobre el dom de js

//DOM
//Document Object Model

//El DOM es la representacion de un documento HTML/XML que se carga en el navegador y se convierte en un arbol de nodos
//El DOM es una interfaz de programacion de aplicaciones(API) para documentos HTML y XML
//El DOM representa la pagina web para el navegador y permite cambiar el contenido de la pagina web

//el objeto document representa el documento HTML

document.body.innerHTML = "Hola Mundo"; //cambia el contenido de la pagina web


//Seleccionado elementos del DOM

//getElementById()
// document.getElementById("demo").innerHTML = "Hola Mundo";
document.getElementsByClassName("demo").innerHTML = "Hola Mundo";
document.getElementsByTagName("p").innerHTML = "Hola Mundo";

var elem = document.getElementById("demo"); //selecciona un elemento por su id
elem.innerHTML = "Hello World!"; //cambia el contenido del elemento


// Seleccionando elementos , puede  que hayan varios elementos con la misma clase o etiqueta
var arr = document.getElementsByClassName("demo");
//accessing the second element
arr[1].innerHTML = "Hi";

/*
Seleccionando Elementos

5
49
Ver idioma original
.
Configuración de idioma
Seleccionando Elementos
El método getElementsByClassName() devuelve una colección de todos los elementos en el documento con el nombre de clase especificado.

Por ejemplo, si nuestra página HTML contiene tres elementos con class="demo", el siguiente código devolverá todos esos elementos como una matriz: 

var arr = document.getElementsByClassName("demo");
//accessing the second element
arr[1].innerHTML = "Hi";
JS
De manera similar, el método getElementsByTagName devuelve todos los elementos del nombre de etiqueta especificado como un array.

El siguiente ejemplo obtiene todos los elementos de párrafo de la página y cambia su contenido:

<p>hi</p>
<p>hello</p>
<p>hi</p>
<script>
var arr = document.getElementsByTagName("p");
for (var x = 0; x < arr.length; x++) {
  arr[x].innerHTML = "Hi there";
}
</script>
JS
El script resultará en el siguiente HTML:

<p>Hi there</p>
<p>Hi there</p>
<p>Hi there</p>
HTML
Usamos la propiedad length del array para recorrer todos los elementos seleccionados en el ejemplo anterior.

Continuar

*/


//Cambiando atributos de elementos, sirve para cambiar el valor de los atributos de un elemento

document.getElementById("image").src = "landscape.jpg"; //cambia el atributo src de una imagen

<img id="myimg" src="orange.png" alt="" />
var el = document.getElementById("myimg");
el.src = "apple.png";



//ejemplo cambiar todas las imagenes de la pagina
var x = document.getElementsByTagName("img");
for (var i = 0; i < x.length; i++) {
  x[i].src = "landscape.jpg";
}

//agregando y eliminando elementos
/*Utiliza los siguientes métodos para crear nuevos nodos:

element.cloneNode() clona un elemento y devuelve el nodo resultante.

document.createElement(element) crea un nuevo nodo de elemento. 

document.createTextNode(text) crea un nuevo nodo de texto. */

var p = document.createElement("p");
var node = document.createElement("Some new text");
p.appendChild(node);


/*Esto creará un nuevo nodo de texto, pero no aparecerá en el documento hasta que lo agregues a un elemento existente con uno de los siguientes métodos:

element.appendChild(newNode) agrega un nuevo nodo hijo a un elemento como el último nodo hijo.

element.insertBefore(node1, node2) inserta node1 como un hijo antes de node2. */


//Eliminar elementos
//calling the function in window.onload to make sure the HTML is loaded
window.onload = function() {
  var parent = document.getElementById("demo");
  var child = document.getElementById("p1");
  parent.removeChild(child);
};


//Reemplazar elementos

window.onload = function() {
  var p = document.createElement("p");
  var node = document.createTextNode("This is new");
  p.appendChild(node);

  var parent = document.getElementById("demo");
  var child = document.getElementById("p1");
  parent.replaceChild(p, child);
};


//Animaciones 
//ver carpeta de animaciones

/*Animaciones
Para crear una animación, necesitamos cambiar las propiedades de un elemento a intervalos pequeños de tiempo. Podemos lograr esto utilizando el método setInterval(), que nos permite crear un temporizador y llamar a una función para cambiar las propiedades repetidamente a intervalos definidos (en milisegundos).

Por ejemplo:

var t = setInterval(move, 500);
JS
Este código crea un temporizador que llama a una función move() cada 500 milisegundos.

Ahora necesitamos definir la función move(), que cambia la posición de la caja.

// starting position
var pos = 0; 
//our box element
var box = document.getElementById("box");

function move() {
  pos += 1;
  box.style.left = pos+"px"; //px = pixels
}
JS
 */

//Eventos
//Los eventos son acciones que ocurren en el navegador que pueden ser detectadas por el script para ejecutar código.
// onclick, onmouseover, onmouseout, onload, onkeydown, onkeyup, onfocus, onblur, onchange, onsubmit, onresize, onscroll, onselect, onerror, onabort, onunload

//Ejemplo de evento
//<button onclick="displayDate()">The time is?</button>
//<script>
function displayDate() {
  document.getElementById("demo").innerHTML = Date();
  alert("Hola Mundo")
}
//</script>


/*ventos 
Los eventos onload y onunload se activan cuando el usuario entra o sale de la página. Estos pueden ser útiles al realizar acciones después de que la página se haya cargado. 

<body onload="doSomething()">
HTML
De manera similar, el evento window.onload se puede usar para ejecutar código después de que se haya cargado toda la página.

window.onload= function() {
   //some code
}
JS
El evento onchange se utiliza principalmente en cuadros de texto. El manejador de eventos se llama cuando el texto dentro del cuadro de texto cambia y se pierde el foco del elemento.

Por ejemplo:

¿Atascado?
HTML
JS
123456789 */


element.addEventListener("click", myFunction); //agrega un evento a un elemento cuando se hace click

element.addEventListener("mouseover", myFunction);  //agrega un evento a un elemento cuando el mouse pasa por encima

function myFunction() { //funcion que se ejecuta al hacer click
  alert("Hello World!");
}


//Propagacion de eventos
/*Hay dos maneras de propagación de eventos en el DOM de HTML: burbujeo y captura.

La propagación de eventos permite la definición del orden de los elementos cuando ocurre un evento. Si tienes un elemento <p> dentro de un elemento <div>, y el usuario hace clic en el elemento <p>, ¿Cuál evento "click" del elemento se debería manejar primero?

En burbujeo, el evento del elemento más interno se maneja primero y luego el evento del elemento externo. El evento click del elemento <p> se maneja primero, seguido por el evento click del elemento <div>.

En captura, el evento del elemento más externo se maneja primero y luego el interno. El evento click del elemento <div> se maneja primero, seguido por el evento click del elemento <p>.

La captura desciende hacia abajo en el DOM.

El burbujeo asciende hacia arriba en el DOM.*/

/*Captura vs. Propagación 
 

El método addEventListener() te permite especificar el tipo de propagación con el parámetro "useCapture".

addEventListener(event, function, useCapture)
JS
El valor predeterminado es false, lo que significa que se utiliza la propagación de burbujeo; cuando el valor se establece en true, el evento utiliza la propagación de captura.

//Capturing propagation
elem1.addEventListener("click", myFunction, true); 

//Bubbling propagation
elem2.addEventListener("click", myFunction, false); */

//Deslizador de imágenes
//ver carpeta de slider


//Validacion de formularios
<form onsubmit="return validate()" method="post">
  Number: <input type="text" name="num1" id="num1" />
  <br />
  Repeat: <input type="text" name="num2" id="num2" />
  <br />
  <input type="submit" value="Submit" />
</form>

function validate() {
  var n1 = document.getElementById('num1');
  var n2 = document.getElementById('num2');
  if(n1.value != '' && n2.value != '') {
      if(n1.value == n2.value) {
          return true;
      }
  }
  alert("The values should be equal and not blank");
  return false;
}
//devo de validar que los campos no esten vacios y que sean iguales