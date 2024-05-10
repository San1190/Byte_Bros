--LAS BASES DE LUA
--

print("Hola Mundo")

--Variables
--Las variables en lua son globales por defecto
--Para declarar una variable se hace de la siguiente manera
--variable = valor
--Ejemplo
Variable = 10 --Variable global
print(Variable)

local Variable2 = 20 --Variable local

--Para declarar una variable local se hace de la siguiente manera

local Variable3 = 30
print(Variable3)

--Para declarar una variable global se hace de la siguiente manera
_G.Variable4 = 40
print(Variable4)

--Para declarar una variable de tipo string se hace de la siguiente manera
local Nombre = "Juan"
print(Nombre)

--Para declarar una variable de tipo booleano se hace de la siguiente manera
local Verdadero = true
print(Verdadero)

--Para declarar una variable de tipo numero se hace de la siguiente manera
local Numero = 10
print(Numero)

--Para declarar una variable de tipo tabla se hace de la siguiente manera
local Tabla = {}
print(Tabla)

--Para declarar una variable de tipo funcion se hace de la siguiente manera
local Funcion = function()
    print("Hola Mundo")
end

Funcion()

--Para declarar una variable de tipo nil se hace de la siguiente manera
local Nulo = nil
print(Nulo)


--Operadores
--Los operadores en lua son los siguientes
-- + Suma
-- - Resta
-- * Multiplicacion
-- / Division
-- % Modulo
-- ^ Exponenciacion
-- == Igual
-- ~= Diferente
-- < Menor que
-- > Mayor que
-- <= Menor o igual que
-- >= Mayor o igual que
-- and Y
-- or O
-- not Negacion
-- .. Concatenacion
-- # Longitud de una cadena o tabla

--Ejemplos
local Numero1 = 10
local Numero2 = 20

local Suma = Numero1 + Numero2
print(Suma)

local Resta = Numero1 - Numero2
print(Resta)

local Multiplicacion = Numero1 * Numero2
print(Multiplicacion)

local Division = Numero1 / Numero2
print(Division)

local Modulo = Numero1 % Numero2
print(Modulo)

local Exponenciacion = Numero1 ^ Numero2
print(Exponenciacion)

local Igual = Numero1 == Numero2
print(Igual)

local Diferente = Numero1 ~= Numero2
print(Diferente)

local Menor = Numero1 < Numero2
print(Menor)

local Mayor = Numero1 > Numero2
print(Mayor)

local MenorIgual = Numero1 <= Numero2
print(MenorIgual)

local MayorIgual = Numero1 >= Numero2
print(MayorIgual)

local Y = Verdadero and Verdadero
print(Y)

local O = Verdadero or Verdadero
print(O)

local Negacion = not Verdadero
print(Negacion)

local Concatenacion = Nombre .. " " .. "Perez"
print(Concatenacion)

local Longitud = #Concatenacion --Longitud de una cadena
print(Longitud)

--Condicionales
--Los condicionales en lua son los siguientes
-- if
-- elseif
-- else
-- then
-- end

--Ejemplos
local Numero3 = 30

if Numero3 == 30 then
    print("El numero es 30")
end

if Numero3 == 30 then
    print("El numero es 30")
else
    print("El numero no es 30")
end

if Numero3 == 30 then
    print("El numero es 30")
elseif Numero3 == 40 then
    print("El numero es 40")
else
    print("El numero no es 30 ni 40")
end

--Ciclos
--Los ciclos en lua son los siguientes
-- for
-- while
-- repeat
-- break
-- continue

--Ejemplos
for i = 1, 10 do
    print(i)
end

local i = 1
while i <= 10 do
    print(i)
    i = i + 1
end

repeat
    print(i)
    i = i + 1
until i > 10

for i = 1, 10 do
    if i == 5 then
        break
    end
    print(i)
end

for i = 1, 10 do
    if i == 5 then
        goto continuar -- el goto  es una mala practica en programacion pero en lua se puede usar para saltar a una etiqueta
    end
    print(i)
    ::continuar::
end

--Funciones
--Las funciones en lua se declaran de la siguiente manera
--function nombre(parametros)
--  codigo
--end

--Ejemplos
function Saludar()
    print("Hola Mundo")
end

Saludar()

function Sumar(Numero1, Numero2)
    return Numero1 + Numero2
end

local Resultado = Sumar(10, 20)
print(Resultado)

--Tablas
--Las tablas en lua son arreglos asociativos
--Se declaran de la siguiente manera
--tabla = {clave = valor}

--Ejemplos
local Persona = { nombre = "Juan", apellido = "Perez", edad = 20 }
print(Persona.nombre)
print(Persona.apellido)
print(Persona.edad)

local Persona2 = { nombre = "Maria", apellido = "Lopez", edad = 30 }
print(Persona2.nombre)
print(Persona2.apellido)
print(Persona2.edad)

local Personas = { Persona, Persona2 }
print(Personas[1].nombre)
print(Personas[2].nombre)

--Metodos
--Los metodos en lua se declaran de la siguiente manera
--tabla.metodo = function(parametros)
--  codigo
--end

--Ejemplos
Persona.Saludar = function()
    local love = require("love")
    local Mutex = love.thread.newMutex()
    Mutex:lock()
    print("Hola Mundo")
    Mutex:unlock()
end




--Metodos de string
--Los metodos de string en lua son los siguientes
-- string.byte hace referencia a un caracter en codigo ASCII
-- string.char hace referencia a un caracter en codigo ASCII
-- string.dump hace referencia a la funcion en codigo maquina
-- string.find busca una cadena en otra cadena  y devuelve la posicion
-- string.format formatea una cadena
-- string.gmatch recorre una cadena con un patron
-- string.gsub reemplaza una cadena por otra
-- string.len devuelve la longitud de una cadena
-- string.lower convierte una cadena a minusculas
-- string.match busca una cadena en otra cadena
-- string.rep repite una cadena
-- string.reverse invierte una cadena
-- string.sub extrae una subcadena
-- string.upper convierte una cadena a mayusculas

--Ejemplos
local Cadena = "Hola Mundo"
print(string.byte(Cadena, 1))
print(string.char(72))
print(string.dump(Saludar))
print(string.find(Cadena, "Mundo"))
print(string.format("Hola %s", "Mundo"))
for i in string.gmatch(Cadena, "%a+") do
    print(i)
end
print(string.gsub(Cadena, "Mundo", "Lua"))
print(string.len(Cadena))
print(string.lower(Cadena))
print(string.match(Cadena, "%a+"))
print(string.rep(Cadena, 2))
print(string.reverse(Cadena))
print(string.sub(Cadena, 1, 4))
print(string.upper(Cadena))
