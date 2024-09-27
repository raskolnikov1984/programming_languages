
const almuerzo = (proteina, verdura) => {
  return `${proteina} ${verdura}`
}

const greeting = function(name){
  return `Hi, ${name}`;
}

// Arrow function - explicit return
const arroGreting = (name) => {
  return `Hi, ${name}`;
}

// Arrow function - implicit return
const arroGretingImpliciting = (name) => {`Hi, ${name}`}

// Lexical Binding

const finctionalCharacter = {
  name: 'Uncle Ben',
  messageWithTradicionalFunction: function (message){
    console.log(`${this.name} says: ${message}`)
  },
  messageWithArrowFunction: (message) => {console.log(`${this.name} says: ${message}`)},
}


finctionalCharacter.messageWithTradicionalFunction('Un Gran Poder conlleva una gran responsabilidad');
finctionalCharacter.messageWithArrowFunction('Beware of Doctor Octopus');
