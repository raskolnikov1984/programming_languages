/* Swicth */

let fruta = "Papayas"
switch (fruta){
  case "Naranjas":
    // Codigo a Ejecutar
    console.log("Precio 20K")
    break;
  case "Manzanas":
    // Codigo a Ejecutar
    console.log("Precio 30K")
    break;
  case "Mangos":
  case "Papayas":
    console.log("Precio 50K")
    break;
  default:
    // Codigo por Defecto
    console.log("Precio 5K")
}
