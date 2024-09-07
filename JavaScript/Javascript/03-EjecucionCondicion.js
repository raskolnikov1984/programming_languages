let edad = "a";

if (edad >= 18){
  console.log("Es Mayor de Edad");
} else if (edad < 18){
  console.log("Es Menor de Edad");
}else{
  console.log("No identificado");
}


/* Adivina el Numero */

const numeroSecreto = Math.floor(Math.random() * 10 + 1);
const numeroJugador = parseInt(
  prompt("Adivina el numero secreto entre el 1 y el 10")
);

console.log(`Este es el numero con el que juegas ${numeroJugador}`);
if (numeroJugador === numeroSecreto){
  console.log("Adivinaste El Numero Secreto");
} else if(numeroJugador < numeroSecreto){
  console.log("El numero es demasiado Bajo");
}else if(numeroJugador > numeroSecreto){
  console.log("El numero es demasiado Alto");
}else{
  console.log("No Adivinaste El Numero Secreto");
}
