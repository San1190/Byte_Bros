# Bienvenidos a la documentación de Ruby
# Ruby es un lenguaje de programación de alto nivel, interpretado, dinámico y orientado a objetos.

# Importaciones
# Para importar un módulo utilizamos la palabra reservada require seguida del nombre del módulo
require "date" # Módulo para trabajar con fechas

# Para mostrar por pantalla un mensaje utilizamos el método puts
puts "Hola Mundo"

# Para declarar una variable utilizamos el símbolo de igualdad
variable = "Hola Mundo"
puts variable

# Para declarar una constante utilizamos la palabra en mayúsculas
CONSTANTE = "Hola Mundo"
puts CONSTANTE

# Sentencias de control
# Ruby soporta las sentencias de control típicas de la mayoría de los lenguajes de programación

# if
if 1 < 2
  puts "1 es menor que 2"
end

# if else
if 1 > 2
  puts "1 es mayor que 2"
else
  puts "1 no es mayor que 2"
end

# if elsif
if 1 > 2
  puts "1 es mayor que 2"
elsif 1 < 2
  puts "1 es menor que 2"
end

# unless
unless 1 > 2
  puts "1 no es mayor que 2"
end

# unless else
unless 1 < 2
  puts "1 no es menor que 2"
else
  puts "1 es menor que 2"
end

# case
case 1
when 1
  puts "1"
when 2
  puts "2"
else
  puts "No es ni 1 ni 2"
end

# Ciclos
# Ruby soporta los ciclos típicos de la mayoría de los lenguajes de programación

# while
i = 0
while i < 5 # Mientras i sea menor a 5
  puts i
  i += 1
end

# until
i = 0
until i == 5 # Hasta que i sea igual a 5
  puts i
  i += 1
end

# for
for i in 0..4 # 0..4 es un rango como en Python
  puts i
end

# each, parecido al forEach de JavaScript
(0..4).each do |i|
  puts i
end

# times, mostrara el valor de i desde 0 hasta 4
5.times do |i|
  puts i
end

# Métodos
# Para definir un método utilizamos la palabra reservada def seguida del nombre del método
def metodo
  puts "Hola Mundo"
end

# Para llamar a un método simplemente escribimos su nombre
metodo

# Para definir un método con parámetros simplemente los escribimos entre paréntesis
def metodo_con_parametros(parametro)
  puts parametro
end

# Para llamar a un método con parámetros simplemente los escribimos entre paréntesis
metodo_con_parametros("Hola Mundo")

# Para definir un método con parámetros por defecto simplemente los escribimos seguidos de un igual y el valor por defecto
def metodo_con_parametros_por_defecto(parametro = "Hola Mundo")
  puts parametro
end

# Funciones lambda
# Para definir una función lambda utilizamos la palabra reservada lambda seguida de la lista de parámetros entre barras verticales y el cuerpo de la función entre llaves
lambda = lambda { |parametro| puts parametro }

# Para llamar a una función lambda simplemente escribimos su nombre seguido de los parámetros entre paréntesis
lambda.call("Hola Mundo")

# Clases
# Para definir una clase utilizamos la palabra reservada class seguida del nombre de la clase

class Clase
  # Para definir un constructor utilizamos el método initialize
  def initialize(parametro)
    @parametro = parametro
  end

  # Para definir un método de instancia simplemente lo escribimos, como un this en java o self en python
  def metodo
    puts @parametro
  end

  # Para definir un método de clase simplemente lo escribimos seguido de la palabra reservada self
  def self.metodo_de_clase
    puts 4 + 4
  end
end

# Para instanciar una clase simplemente escribimos su nombre seguido de los parámetros entre paréntesis
clase = Clase.new("Hola Mundo")

# Para llamar a un método de instancia simplemente escribimos su nombre
clase.metodo

# Para llamar a un método de clase simplemente escribimos su nombre seguido de un punto y el nombre del método
Clase.metodo_de_clase

# Herencia
# Para definir una clase que herede de otra simplemente escribimos el nombre de la clase seguido de un menor que y el nombre de la clase de la que queremos heredar

class ClaseHija < Clase
  def metodo_hijo
    puts "Hola Mundo"
  end
end

# Para instanciar una clase hija simplemente escribimos su nombre seguido de los parámetros entre paréntesis
clase_hija = ClaseHija.new("Hola Mundo")

# Para llamar a un método de la clase hija simplemente escribimos su nombre
clase_hija.metodo_hijo


# Módulos
# Para definir un módulo utilizamos la palabra reservada module seguida del nombre del módulo
# Los módulos son una forma de agrupar métodos, clases y constantes, como una libreria de la que podras hacer uso en cualquier parte de tu código

module Modulo
  # Para definir un método de módulo simplemente lo escribimos
  def self.metodo
    puts "Hola Mundo"
  end
end

# Para llamar a un método de módulo simplemente escribimos su nombre
Modulo.metodo

# Mixins
# Para incluir un módulo en una clase simplemente escribimos include seguido del nombre del módulo

module Mixin
  def metodo
    puts "Hola Mundo"
  end
end

class ClaseMixin
  include Mixin
end

# Para instanciar una clase
clase_mixin = ClaseMixin.new

# Para llamar a un método de un módulo simplemente escribimos su nombre
clase_mixin.metodo

# Excepciones
# Para lanzar una excepción utilizamos la palabra reservada raise seguida del nombre de la excepción
# raise "Error", no lo llamamos que sino peta

# Para capturar una excepción utilizamos la palabra reservada begin seguida del bloque de código que queremos ejecutar y la palabra reservada rescue seguida del bloque de código que queremos ejecutar en caso de que se lance una excepción
begin # Try
  puts 1 / 0
rescue => exception # Catch
  puts "Error", exception
ensure # Finally
  puts "Siempre se ejecuta"
end


# Para definir una excepción utilizamos la palabra reservada class seguida del
# nombre de la excepción y la palabra reservada Exception

class Excepcion < Exception
end

# Para lanzar una excepción utilizamos la palabra reservada raise seguida del nombre de la excepción
# raise Excepcion.new("Error")

# Para capturar una excepción utilizamos la palabra reservada begin seguida del bloque de código que queremos ejecutar y la palabra reservada rescue seguida del bloque de código que queremos ejecutar en caso de que se lance una excepción
begin
  raise Excepcion.new("Error")
rescue Excepcion => e
  puts e.message
end

# Strings y símbolos
# Ruby soporta strings y símbolos
# Metodos utiles para trabajar con strings

# Para concatenar strings utilizamos el operador +
puts "Hola " + "Mundo"

# Para interpolar strings utilizamos el operador #
puts "Hola #{ "Mundo" }"

# Para obtener la longitud de un string utilizamos el método length
puts "Hola Mundo".length

# Para convertir un string a mayúsculas utilizamos el método upcase
puts "Hola Mundo".upcase

# Para convertir un string a minúsculas utilizamos el método downcase
puts "Hola Mundo".downcase

# Para convertir un string a un array utilizamos el método split
lista = "Hola Mundo".split(" ")
puts lista





# Fechas
# Para trabajar con fechas utilizamos el módulo Date

# Para obtener la fecha actual utilizamos el método today
fecha = Date.today

# Para obtener el año utilizamos el método year
puts fecha.year

# Para obtener el mes utilizamos el método month
puts fecha.month

# Para obtener el día utilizamos el método day
puts fecha.day

# Para obtener el día de la semana utilizamos el método wday
puts fecha.wday

# Para obtener el día del año utilizamos el método yday
puts fecha.yday


# Números aleatorios
# Para trabajar con números aleatorios utilizamos el módulo Random ya incluido en Ruby, no hay que importarlo

# Para obtener un número aleatorio utilizamos el método rand
numero = Random.rand(10)
puts "Numero aleatorio: #{numero}"

# Para obtener un número aleatorio en un rango utilizamos el método rand
numero = Random.rand(1..10)
puts "Numero aleatorio: #{numero}"


# Arrays

# Para definir un array utilizamos corchetes
array = [1, 2, 3, 4, 5]

# Para obtener un elemento de un array utilizamos corchetes y el índice del elemento
puts array[0]

# Para obtener la longitud de un array utilizamos el método length
puts array.length

# Para obtener el primer elemento de un array utilizamos el método first
puts array.first

# Para obtener el último elemento de un array utilizamos el método last
puts array.last

# Para obtener un rango de elementos de un array utilizamos corchetes y el rango de elementos
puts array[0..2]

# Para obtener un rango de elementos de un array utilizamos el método slice
puts array.slice(0, 2)

# Para añadir un elemento a un array utilizamos el método push
array.push(6)

# Para eliminar un elemento de un array utilizamos el método pop
array.pop

# Para añadir un elemento al principio de un array utilizamos el método unshift
array.unshift(0)

# Para eliminar un elemento del principio de un array utilizamos el método shift
array.shift

# Para recorrer un array utilizamos el método each
array.each do |elemento|
  puts elemento
end

# Para recorrer un array con índice utilizamos el método each_with_index
array.each_with_index do |elemento, indice|
  puts "#{indice}: #{elemento}"
end

# Para recorrer un array en orden inverso utilizamos el método reverse_each
array.reverse_each do |elemento|
  puts elemento
end

# Para ordenar un array utilizamos el método sort
puts array.sort

# Para ordenar un array en orden inverso utilizamos el método reverse
puts array.reverse

# Para obtener un array sin elementos duplicados utilizamos el método uniq
puts array.uniq

# Para aleatorizar un array utilizamos el método shuffle
puts array.shuffle


# Hashes
hashMap = {
  "key" => "value",
  "key2" => "value2"
}

# Para obtener un valor de un hash utilizamos corchetes y la clave del valor
puts hashMap["key"]

# Para obtener las claves de un hash utilizamos el método keys
puts hashMap.keys

# Ejemplo de recorrer el map
hashMap.each do |key, value|
  puts "#{key}: #{value}"
end


# Para interacción con el sistema operativo
# Para ejecutar un comando del sistema operativo utilizamos el método system
system("ls")

# Para obtener la salida de un comando del sistema operativo utilizamos el método ``
puts `ls`

# Para obtener la salida de un comando del sistema operativo utilizamos el método %x
# puts %x(ls) no lo llamamos que sino peta

# Para obtener el directorio actual utilizamos el método pwd
# puts Dir.pwd no lo llamamos que sino peta

# Para cambiar de directorio utilizamos el método chdir
Dir.chdir("/") # change directory
puts Dir.pwd # print working directory

# Para obtener los archivos de un directorio utilizamos el método entries
puts Dir.entries("/")
puts "Archivos txt: ", Dir.entries("/").select { |file| file.end_with?(".txt") } # Solo los archivos que terminen en .txt
puts  "Archivos txt: " ,`ls | grep .txt` # Solo los archivos que terminen en .txt

# Para crear un directorio utilizamos el método mkdir
Dir.mkdir("directorio")

# Para eliminar un directorio utilizamos el método rmdir
Dir.rmdir("directorio")

# Para obtener el contenido de un archivo utilizamos el método read
puts File.read("archivo.txt")

# Para escribir en un archivo utilizamos el método write
File.write("archivo.txt", "Hola Mundo")

# Para añadir al final de un archivo utilizamos el método append
File.open("archivo.txt", "a") do |file| # with open("archivo.txt", "a") as file: # Python
  file.write("Hola Mundo")
end

# Para eliminar un archivo utilizamos el método delete
File.delete("archivo.txt")

# Para renombrar un archivo utilizamos el método rename
File.rename("archivo.txt", "archivo2.txt")

# Para copiar un archivo utilizamos el método copy
File.copy("archivo2.txt", "archivo3.txt")

# Para mover un archivo utilizamos el método move
File.move("archivo3.txt", "directorio/archivo3.txt")

# Para obtener la fecha de creación de un archivo utilizamos el método ctime
puts File.ctime("archivo2.txt")
