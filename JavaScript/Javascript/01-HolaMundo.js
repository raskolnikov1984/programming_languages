// Print
console.log("Hola Mundo de JavaScript");

// Declaracion de Variables

// let: Variables que van a cambiar en el tiempo
// const: Variables Constantes

// Lo No Permitido
let c = 'woody';
let cda = 'woody';
let pcAndy = 'woody';

// Lo Permitido
let cajaDeAndy = "woody";
let primerTrasteoDeAndy = "woody";

// Uso de const
const PI = 3.141516;

// Tipos de Datos
// String
let nombre = 'Tere';
let apellido = 'Alcaraz';
// Interpolacion de Variables
let nombreCompleto = `${nombre} ${apellido}`;
let nombreCompleto2 = nombre + apellido;

/*
 * Metodos Strings
 */
console.log("Longitud de Cadena", nombreCompleto.length)
console.log("Metodo UpperCase", nombreCompleto.toUpperCase())
console.log("Metodo LowerCase", nombreCompleto.toLowerCase())
console.log("Metodo Slice", nombreCompleto.substring(0,5))
// Numbero
let edad = 12;

/*
 * Metodos de Numero
 */

/*Entero y Decimal*/
const entero = 42;
const decimal = 3.14;
console.log("Metodo Comprobacion de Typo ", typeof entero, typeof decimal)

/*Notacion Cientifica*/
const cientifico = 5e3;
console.log("Numero Cientifico", cientifico)
/*Infinitos y NaN*/
const infinito = Infinity
console.log("El Infinito", infinito)
const noEsUnNumero = NaN
console.log("No An Number", noEsUnNumero)

/*Operaciones arimeticas*/
console.log("Operaciones Aritmeticas", entero + decimal, entero - decimal, entero * decimal, 4 / 2, 3 % 2, 2 ** 2);

// PRECISION
let suma = 0.1 + 0.2
console.log("Redondeo", suma.toFixed(2));

/* Comparacion Estricta */

console.log("Comparacion Estricta", suma.toFixed(1) === 0.3)


/*Operaciones Math*/
console.log("Raiz Cuadrada", Math.sqrt(16))
console.log("Valor Absoluto", Math.abs(-7))
console.log("Aleatorio", Math.random())

// Boolean
let esMayorDeEdad = true;
// Null
let noHayValor = null;
// Undefined
let noDefinido = undefined;
// symbol
let simboloUnico = Symbol('unico');
// Bigintw
let numeroGrande = 2n
// Complejo

/*Coercion y Casting */
const numero = 2
const booleano = true
console.log("Conversion de Tipos", numero + booleano)

/*Conversion Explicita
 * String()
 * Number()
 * Boolean()
 */

let carro = {
  marco: 'Tesla',
  modelo: 'Model S'
}

// Array
let frutas = ['manzana', 'banano', 'uvas'];

// Funciones
function saludar(nombreCompleto){
  console.log(`Saludos Querio Amigx ${nombreCompleto}`);
}

// Invocando la funcion Saludar
saludar(nombreCompleto);
