/* How create an Array */

const fruits = Array('apple', 'banana', 'orange');
console.log(fruits);

const justOneNumber = Array(12)
console.log(justOneNumber);

const number = Array(1, 2, 3, 4, 5)
console.log(number);

const oneNumber = [4]
console.log(oneNumber);

const emptyArray = []
console.log(emptyArray);

const sports = ['A', 'B', 'C'];
console.log(sports);

const recipeIngredients = [
  'Flour',
  true,
  2,
  {
    ingredients: 'Milk', quantity: '1 cup'
  },
  false
]

console.log(recipeIngredients);
console.log(sports[0]);
console.log(sports.length);

sports.push('D');
console.log(sports);
console.log(sports.concat(['E', 'F']));


const isArray = Array.isArray(fruits)
console.log(isArray)


const numbers = [1,2,4,5];
let sum = 0;

for (let i = 0; i < numbers.length; i++){
  sum += numbers[i];
}

console.log(sum);
