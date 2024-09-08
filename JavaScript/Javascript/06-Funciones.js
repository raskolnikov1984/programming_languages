function sum(a, b){
  return a + b;
}

sum(3, 5)

function calculatedDiscountedPrice (price, discountPercentage) {
  const discount = (price * discountPercentage) / 100;
  const priceWithDiscount = price - discount;

  return priceWithDiscount;
}

const originalPrice = 100;
const discountPercentage = 20;
const finalPrice = calculatedDiscountedPrice(originalPrice, discountPercentage);

console.log('Original Price: $' + originalPrice);
console.log('Discount: ' + discountPercentage + '%');
console.log('Price with discount: $' + finalPrice);


/* Callback */

function a(){}
function b(){}

b(a)

/* Retornar Funciones */

function a (){
  function b (){}
  return b;
}

/* Asignar Funciones A variables */

// const a = function(){}

// /* Propiedades y Metodos */
// function a (){}
// const obj = {}

// a.call(obj);


function a (){
  function b (){}
}

/* Funciones en Objetos */

const rocket = {
  name: 'Falcon 9',
  launchMessage: function launchMessage(){
    console.log('Lunch!!');
  }
}

rocket.launchMessage()
