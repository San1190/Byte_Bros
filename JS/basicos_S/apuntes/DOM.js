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


