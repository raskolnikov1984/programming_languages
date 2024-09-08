/* For */

let list = ["eat", "sleep", "code", "repeat"];

for (let i = 0; i < list.length; i++ ){
  console.log(list[i]);
}

/* For of */

let canasta = ["manzana", "pera", "naranja", "uva"];

for (fruta of canasta){
  console.log(fruta);
}

/* For In */

const listaDeCompras = {
  manzana: 5,
  pera: 3,
  naranja: 2,
  uva: 1
}

for (fruta in listaDeCompras){
  console.log(fruta);
}

for (fruta in listaDeCompras){
  console.log(`${fruta} : ${listaDeCompras[fruta]}`);
}


/* While */

let contador = 0;

while (contador < 10){
  console.log(contador);
  contador++;
}

let contador1 = 0;
do {
  console.log(contador1);
  contador1++;
}while (contador1 < 10);

/* Do While */
