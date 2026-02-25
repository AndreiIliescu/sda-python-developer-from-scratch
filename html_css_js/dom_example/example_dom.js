// DOM Model

// Get element by id
const element = document.getElementById("ex1");
console.log(element); // <div id="ex1">Hello</div>
console.log(element.innerText); // Hello

element.innerText = "Sunt in ceata";
element.style = "color: red";

// Get element by class
const elements_1 = document.getElementsByClassName("c1");
console.log(elements_1.length); // 2

// Get element by tag
const elements_2 = document.getElementsByTagName("li");
for (let idx = 0; idx < elements_2.length; idx++) {
  console.log(elements_2[idx]); // <li>Hello From</li> and then <li>DOM</li> will appear on the screen
}

// Query Selector
const qs_element = document.querySelector(".big-text");
console.log(qs_element); // <p class="big-text">Query selector example</p>

const qs_elements = document.querySelectorAll(".big-text");
console.log(qs_elements); // NodeList(2) [p.big-text, section.big-text]

// Creare de elemente HTML
const father = document.getElementById("some-id");
const child = document.createElement("div");
child.innerText = "Child of div"

father.appendChild(child);

