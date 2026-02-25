// Event Listener on click
function displayText() {
  console.log("The button has been clicked!");
  document
    .getElementById("id-button")
    .removeEventListener("click", displayText);
}

document.getElementById("id-button").addEventListener("click", displayText);

// Convertire la JSON
var person = {
  name: "John",
  surname: "Doe",
};
console.log(person)

let strJSON = JSON.stringify(person);
console.log(strJSON)

let thisWillBeAnObject = JSON.parse(strJSON);
console.log(thisWillBeAnObject)
