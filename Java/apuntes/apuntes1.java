//Bienvenido a los apuntes de Java desde cero hasta experto.
//Ojala nunca haber dado esta mierda de lenguaje :), pero bueno, es lo que hay. 
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


public class apuntes1 {
    public static void main(String[] args) {
        //Esto es un comentario de una sola línea
        
        /* Esto es un comentario
        de varias líneas */

        //Variables
        //Las variables son espacios de memoria que se utilizan para almacenar valores.
        //En Java, cada variable debe tener un tipo de datos asociado a ella.
        //Los tipos de datos primitivos son los más básicos y se utilizan para almacenar valores simples.
        //Los tipos de datos primitivos en Java son:
        //byte, short, int, long, float, double, char, boolean

        //Declaración de variables
        int numero = 10;
        double decimal = 10.5;
        char letra = 'a';
        boolean verdadero = true;

        //Operadores
        //Los operadores son símbolos que se utilizan para realizar operaciones sobre variables y valores.
        //Los operadores aritméticos se utilizan para realizar operaciones matemáticas.
        //Los operadores aritméticos en Java son:
        //+ (suma), - (resta), * (multiplicación), / (división), % (módulo)

        //Operadores de asignación
        //Los operadores de asignación se utilizan para asignar valores a variables.
        //Los operadores de asignación en Java son:
        //= (asignación), += (suma y asignación), -= (resta y asignación), *= (multiplicación y asignación), /= (división y asignación), %= (módulo y asignación)

        //Operadores de incremento y decremento
        //Los operadores de incremento y decremento se utilizan para aumentar o disminuir el valor de una variable en una unidad.
        //Los operadores de incremento y decremento en Java son:
        //++ (incremento), -- (decremento)

        //Operadores de comparación
        //Los operadores de comparación se utilizan para comparar dos valores.
        //Los operadores de comparación en Java son:
        //== (igual a), != (diferente de), > (mayor que), < (menor que), >= (mayor o igual que), <= (menor o igual que)

        //Operadores lógicos
        //Los operadores lógicos se utilizan para combinar dos o más expresiones lógicas.
        //Los operadores lógicos en Java son:
        //&& (y lógico), || (o lógico), ! (no lógico)

        //Estructuras de control
        //Las estructuras de control se utilizan para controlar el flujo de un programa.
        //Las estructuras de control en Java son:
        //if, else, else if, switch, while, do while, for, break, continue, return

        //Estructura if
        //La estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera.
        if (numero > 0) {
            System.out.println("El número es positivo");
        }

        //Estructura if else
        //La estructura if else se utiliza para ejecutar un bloque de código si una condición es verdadera y otro bloque de código si la condición es falsa.
        if (numero > 0) {
            System.out.println("El número es positivo");
        } else {
            System.out.println("El número es negativo");
        }

        //Estructura else if
        //La estructura else if se utiliza para evaluar múltiples condiciones.
        if (numero > 0) {
            System.out.println("El número es positivo");
        } else if (numero < 0) {
            System.out.println("El número es negativo");
        } else {
            System.out.println("El número es cero");
        }

        //Estructura switch
        //La estructura switch se utiliza para seleccionar uno de varios bloques de código para ejecutar.
        switch (numero) {
            case 1:
                System.out.println("El número es uno");
                break;
            case 2:
                System.out.println("El número es dos");
                break;
            default:
                System.out.println("El número es otro");
        }

        //Estructura while
        //La estructura while se utiliza para ejecutar un bloque de código mientras una condición sea verdadera.
        while (numero > 0) {
            System.out.println("El número es positivo");
            numero--;
        }

        //Estructura do while
        //La estructura do while se utiliza para ejecutar un bloque de código al menos una vez y luego repetirlo mientras una condición sea verdadera.
        do {
            System.out.println("El número es positivo");
            numero--;
        } while (numero > 0);

        //Estructura for
        //La estructura for se utiliza para ejecutar un bloque de código un número específico de veces.
        for (int i = 0; i < 5; i++) {
            System.out.println("El número es " + i);
        }

        //Estructura break
        //La estructura break se utiliza para salir de un bucle.
        for (int i = 0; i < 5; i++) {
            if (i == 3) {
                break;
            }
            System.out.println("El número es " + i);
        }
        
        //Estructura continue
        //La estructura continue se utiliza para saltar a la siguiente iteración de un bucle.
        for (int i = 0; i < 5; i++) {
            if (i == 3) {
                continue;
            }
            System.out.println("El número es " + i);
        }

        //Estructura return
        //La estructura return se utiliza para devolver un valor desde un método.
        int resultado = sumar(5, 3);
        System.out.println("El resultado es " + resultado);


        //Manejo de excepciones
        //Las excepciones son errores que ocurren durante la ejecución de un programa.
        //Las excepciones en Java se dividen en dos categorías: excepciones comprobadas y excepciones no comprobadas.
        //Las excepciones comprobadas son excepciones que se deben manejar en tiempo de compilación.
        //Las excepciones no comprobadas son excepciones que se pueden manejar en tiempo de ejecución.
        //Las excepciones en Java se manejan utilizando bloques try, catch y finally.
        //El bloque try se utiliza para probar un bloque de código en busca de excepciones.
        //El bloque catch se utiliza para manejar las excepciones que se producen en el bloque try.
        //El bloque finally se utiliza para ejecutar un bloque de código después de que se haya producido una excepción.
        //Las excepciones en Java se pueden lanzar utilizando la palabra clave "throw".
        //Las excepciones en Java se pueden crear utilizando la palabra clave "throws".
        
        

        //Ejemplo de excepción
        try {
            int[] numeros = {1, 2, 3};
            System.out.println(numeros[3]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("El índice está fuera de rango");
        } finally {
            System.out.println("El programa ha terminado");
        }


        //Funciones
        //Las funciones se utilizan para dividir un programa en bloques de código más pequeños y reutilizables.
        //Las funciones en Java se definen con la palabra clave "static" seguida del tipo de datos de retorno, el nombre de la función, y los parámetros entre paréntesis.
        //El tipo de datos de retorno de una función puede ser cualquier tipo de datos primitivo o un objeto.
        //Los parámetros de una función son variables que se utilizan para pasar valores a la función.
        //Una función puede tener cero o más parámetros.
        //Una función puede devolver un valor utilizando la palabra clave "return".
        //Una función puede devolver un valor de cualquier tipo de datos primitivo o un objeto.
        //Una función puede devolver múltiples valores utilizando un objeto o un array.


        // Polimorfismo
        // El polimorfismo es un concepto que permite tratar objetos de una clase
        // derivada como objetos de la clase base.
        // El polimorfismo se logra utilizando una referencia de la clase base para
        // referenciar un objeto de la clase derivada.
        // El polimorfismo permite llamar a los métodos de la clase derivada utilizando
        // la referencia de la clase base.
        // El polimorfismo se basa en el principio de sustitución de Liskov.
        // El principio de sustitución de Liskov establece que un objeto de una clase
        // derivada debe poder ser tratado como un objeto de la clase base.
        // El polimorfismo es una característica fundamental de la programación
        // orientada a objetos.

        // Ejemplo de polimorfismo
        //Persona persona = new Empleado();
        // persona.nombre = "Juan";
        // persona.edad = 30;
        // persona.saludar();
        // ((Empleado) persona).trabajar();


      


    }
    //Ejemplo de función
    public static int sumar(int a, int b) {
        return a + b;
    }

    //Clases y objetos
    //Las clases y objetos son conceptos fundamentales en la programación orientada a objetos.
    //Una clase es un plano o plantilla para crear objetos.
    //Un objeto es una instancia de una clase.
    //Una clase en Java se define con la palabra clave "class" seguida del nombre de la clase.
    //Un objeto en Java se crea utilizando la palabra clave "new" seguida del nombre de la clase y los paréntesis.
    //Una clase puede tener atributos y métodos.
    //Los atributos de una clase son variables que se utilizan para almacenar datos.
    //Los métodos de una clase son funciones que se utilizan para realizar operaciones.
    //Los atributos y métodos de una clase se acceden utilizando el operador punto ".".
    //Los atributos de una clase pueden ser públicos, privados o protegidos.
    //Los métodos de una clase pueden ser públicos, privados o protegidos.
    //Los atributos públicos se pueden acceder desde cualquier parte del programa.
    //Los atributos privados solo se pueden acceder desde dentro de la clase.
    //Los atributos protegidos se pueden acceder desde dentro de la clase y desde las clases hijas.
    //Los métodos públicos se pueden llamar desde cualquier parte del programa.
    //Los métodos privados solo se pueden llamar desde dentro de la clase.
    //Los métodos protegidos se pueden llamar desde dentro de la clase y desde las clases hijas.

    //Ejemplo de clase
    public class Persona {
        //Atributos
        public String nombre;
        public int edad;

        //Métodos
        public void saludar() {
            System.out.println("Hola, mi nombre es " + nombre);
        }
    }

    //Ejemplo de objeto
    Persona persona = new Persona();
    //persona.nombre = "Juan";
    //persona.edad = 30;
    //persona.saludar();



    //Herencia
    //La herencia es un mecanismo que permite crear una nueva clase a partir de una clase existente.
    //La clase existente se conoce como clase base o superclase.
    //La nueva clase se conoce como clase derivada o subclase.
    //La clase derivada hereda los atributos y métodos de la clase base.
    //La clase derivada puede agregar nuevos atributos y métodos.
    //La clase derivada puede sobrescribir los métodos de la clase base.

    //Ejemplo de herencia
    public class Empleado extends Persona {
        //Atributos
        public double salario;

        //Métodos
        public void trabajar() {
            System.out.println("Estoy trabajando");
        }
    }

    //Ejemplo de objeto
    Empleado empleado = new Empleado();
    //empleado.nombre = "Pedro";
    //empleado.edad = 25;
    //empleado.salario = 1000;
    //empleado.saludar();
    //empleado.trabajar();


    // Abstracción
    // La abstracción es un concepto que permite ocultar los detalles de
    // implementación y mostrar solo la funcionalidad de un objeto.
    // La abstracción se logra utilizando clases abstractas e interfaces.
    // Una clase abstracta es una clase que no se puede instanciar y que puede
    // contener métodos abstractos.
    // Un método abstracto es un método que no tiene implementación y que debe ser
    // implementado por las clases derivadas.
    // Una interfaz es una colección de métodos abstractos que deben ser
    // implementados por las clases que la implementan.
    // La abstracción es una característica fundamental de la programación orientada
    // a objetos.

    // Ejemplo de abstracción
    // public abstract class Figura {
    //     public abstract double area();
    //     public abstract double perimetro();
    // }

    // public class Circulo extends Figura {
    //     private double radio;

    //     public Circulo(double radio) {
    //         this.radio = radio;
    //     }

    //     public double area() {
    //         return Math.PI * radio * radio;
    //     }

    //     public double perimetro() {
    //         return 2 * Math.PI * radio;
    //     }
    // }

    // public class Cuadrado extends Figura {
    //     private double lado;
        
    //     public Cuadrado(double lado) {
    //         this.lado = lado;
    //     }
        
    //     public double area() {
    //         return lado * lado;
    //     }


    //     public double perimetro() {
    //         return 4 * lado;
    //     }
    // }

    // Map, tabla hash, diccionario
    // Un mapa es una colección de pares clave-valor.
    // Cada clave está asociada a un valor.
    // Las claves de un mapa son únicas.
    // Los valores de un mapa pueden ser duplicados.
    // Un mapa se puede utilizar para almacenar y recuperar datos de forma eficiente.
    // En Java, un mapa se puede implementar utilizando la interfaz Map y las clases HashMap, TreeMap y LinkedHashMap.
    // La interfaz Map define los métodos para trabajar con mapas.
    // La clase HashMap implementa un mapa utilizando una tabla hash.
    // La clase TreeMap implementa un mapa utilizando un árbol binario de búsqueda.
        
    // hay que importar la clase Map
    //import java.util.Map;
    // hay que importar la clase HashMap
    //import java.util.HashMap;
    // Ejemplo de mapa
    public static void  ejemloMap(String[] args) {
        // Crear un mapa
        Map<String, Integer> mapa = new HashMap<>();
        
        // Agregar elementos al mapa
        mapa.put("uno", 1);
        mapa.put("dos", 2);
        mapa.put("tres", 3);
        
        // Recorrer el mapa
        for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
            String clave = entry.getKey();
            Integer valor = entry.getValue();
            System.out.println(clave + " = " + valor);
        }
        
        // Obtener un valor del mapa
        Integer valor = mapa.get("dos");
        System.out.println("El valor es " + valor);
        
        // Verificar si una clave existe en el mapa
        boolean existeClave = mapa.containsKey("cuatro");
        System.out.println("La clave existe " + existeClave);
        
        // Verificar si un valor existe en el mapa
        boolean existeValor = mapa.containsValue(4);
        System.out.println("El valor existe " + existeValor);
        
        // Eliminar un elemento del mapa
        mapa.remove("tres");
        
        // Vaciar el mapa
        mapa.clear();
    }

    // Listas
    // Una lista es una colección de elementos ordenados.
    // Los elementos de una lista se pueden acceder por su índice.
    // Los índices de una lista comienzan en cero.
    // Una lista se puede utilizar para almacenar y recuperar datos de forma eficiente.
    // En Java, una lista se puede implementar utilizando la interfaz List y las clases ArrayList, LinkedList y Vector.
    // La interfaz List define los métodos para trabajar con listas.
    // La clase ArrayList implementa una lista utilizando un array dinámico.
    // La clase LinkedList implementa una lista utilizando una lista doblemente enlazada.
    // La clase Vector implementa una lista utilizando un array dinámico sincronizado.

    // hay que importar la clase List
    //import java.util.List;
    // hay que importar la clase ArrayList
    //import java.util.ArrayList;
    // Ejemplo de lista
    public static void ejemploLista(String[] args) {
        // Crear una lista
        List<Integer> lista = new ArrayList<>();
        
        // Agregar elementos a la lista
        lista.add(1);
        lista.add(2);
        lista.add(3);
        
        // Recorrer la lista
        for (Integer elemento : lista) {
            System.out.println(elemento);
        }
        
        // Obtener un elemento de la lista
        Integer elemento = lista.get(1);
        System.out.println("El elemento es " + elemento);
        
        // Verificar si un elemento existe en la lista
        boolean existeElemento = lista.contains(4);
        System.out.println("El elemento existe " + existeElemento);
        
        // Eliminar un elemento de la lista
        lista.remove(2);
        
        // Vaciar la lista
        lista.clear();
    }



    // Conjuntos
    // Un conjunto es una colección de elementos únicos.
    // Los elementos de un conjunto no tienen un orden específico.
    // Un conjunto se puede utilizar para almacenar y recuperar datos de forma eficiente.
    // En Java, un conjunto se puede implementar utilizando la interfaz Set y las clases HashSet, TreeSet y LinkedHashSet.
    // La interfaz Set define los métodos para trabajar con conjuntos.
    // La clase HashSet implementa un conjunto utilizando una tabla hash.
    // La clase TreeSet implementa un conjunto utilizando un árbol binario de búsqueda.
    // La clase LinkedHashSet implementa un conjunto utilizando una lista doblemente enlazada.

    // hay que importar la clase Set
    //import java.util.Set;
    // hay que importar la clase HashSet
    //import java.util.HashSet;
    // Ejemplo de conjunto
    public static void ejemploConjunto(String[] args) {
        // Crear un conjunto
        Set<Integer> conjunto = new HashSet<>();
        
        // Agregar elementos al conjunto
        conjunto.add(1);
        conjunto.add(2);
        conjunto.add(3);
        
        // Recorrer el conjunto
        for (Integer elemento : conjunto) {
            System.out.println(elemento);
        }
        
        // Verificar si un elemento existe en el conjunto
        boolean existeElemento = conjunto.contains(4);
        System.out.println("El elemento existe " + existeElemento);
        
        // Eliminar un elemento del conjunto
        conjunto.remove(2);
        
        // Vaciar el conjunto
        conjunto.clear();
    }



}













//Con esto terminamos los apuntes de Java desde cero hasta experto. Creo que ya tienes una buena base para empezar a programar en Java.
//Si tienes alguna duda o sugerencia, no dudes en ponerte en contacto conmigo.
//Espero que estos apuntes te hayan sido de ayuda y que te hayan servido para aprender Java.
//¡Buena suerte en tu aprendizaje de Java y en tus futuros proyectos de programación!
//Recomiendo que realices muchos ejercicios prácticos para afianzar los conceptos aprendidos.
//¡Hasta la próxima! :)

//S