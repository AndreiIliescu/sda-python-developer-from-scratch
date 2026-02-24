/*
console.log("Hello World!");

function ab() {
  if (true) {
    var a = 1;
    let b = 2;
  }

  console.log(a); // displays 1 - "a" variable is visible inside the whole function
  // console.log(b);     // causes error - "b is not defined" - "b" ist visible inside
  // "if" block - a block where it was defined.
}

ab(); // function call

console.log(a); // causes "a is not defined" error - "a" variable visible inside
// the `ab` function only

==============================================================================================================================

const global = "global const variable";
let global2 = "global let variable";

function test() {
  console.log(global); // I can display the global variable because it is of global scope
}

test();

==============================================================================================================================

if (1 === 1) {
  console.log("Yes, 1 equals 1!"); // this line will be displayed on the screen
}

if (1 == 1) {
  console.log('Yes, 1 equals 1!')
}

if ([1, 2].includes(1)) {
  console.log("Yes, this array contains the number 1"); // this line will be displayed on the screen
}

if ("") {
  console.log("an empty string is evaluated on false"); // this line will NOT be displayed on the screen
}

if ([]) {
  console.log("an empty array is evaluated on true");
}

if ({}) {
  console.log("an empty object is evaluated on true");
}

if ({} && []) {
  console.log("An empty array and an empty object evaluate themselves as true"); // this line will be displayed on the screen
}

if (null || undefined) {
  console.log("null and undefined evaluate themselves on false"); // this line will NOT be displayed on the screen
}

==============================================================================================================================


const number = 5;

if (number % 5 === 4) {
  console.log("is your number 9?");
} else if (number % 5 === 3) {
  console.log("The remaiander is 3!");
} else if (number > 5) {
  console.log("I dont think its possible");
} else {
  console.log("All 'ifs  were false so we landed here");
}

==============================================================================================================================

function ta_funkcja_zwraca_liczbe_5() {
  console.log("hello from function ta_funkcja_zwraca_liczbe_5()")
}

// const value = 5;
const value = undefined;

switch (value) {
    case 1:
    case 2:
        console.log('works for the "value" equal to 1 or 2');
        break;
    case 1 + 2:
    case "4":
        console.log('works for the "value" equal to 3 lub "4" (string)');
        break;
    case ta_funkcja_zwraca_liczbe_5():
        console.log('works for value == 5');
        break;
    default:
        console.log('works when the "value" is not equial to 1, 2, 3, "4" nor 5');
}

console.log(ta_funkcja_zwraca_liczbe_5())

==============================================================================================================================

for (let i = 0; i < 3; i++) {
    console.log(i);
}

for (; ;) {
} // endless loop

==============================================================================================================================

let numbers = [1, 2, 3, 4];

while (numbers.length > 0) {
    console.log(`I just removed ${numbers.shift()} in a while loop`);
}
Result:
I just removed 1 in a while loop
I just removed 2 in a while loop
I just removed 3 in a while loop
I just removed 4 in a while loop

==============================================================================================================================

(function (a, b) {
    return a + b;
})(10, 20);     // calls the function immediately. Parameters are set using ()
// after the declaration

==============================================================================================================================

const multiply = function (a, b) {
    return a * b;
}

const result = multiply(2, 3);
console.log(result); // 6 will be displayed on the console

==============================================================================================================================
const divide = (dividend, divisor) => dividend / divisor;
const result = divide(5, 2);

console.log(result); // 2.5

==============================================================================================================================

const strings = ['hello', 'hi', 'veryLongOne', 'i'];
strings.sort((strA, strB) => {
    if (strA.length === strB.length) {
        return 0;
    }
    if (strA.length < strB.length) {
        return -1;
    }
    return 1;
}); // the result will be a sorted list: ["i","hi","hello","veryLongOne"]
==============================================================================================================================

['one', 'two', 'three', 'four'].forEach((element, index) => {
    console.log(`element on index ${index} is '${element}'`);
});

The console will display:
element on index 0 is 'one'
element on index 1 is 'two'
element on index 2 is 'three'
element on index 3 is 'four'

==============================================================================================================================

// HOISTING
console.log(foo);
var foo = "Lorem ipsum";


foo = 'hello'
console.log(foo);
var foo = 'Lorem ipsum';
console.log(foo)

add = function (a, b) {
    return a + b;
}
console.log(add(2, 3)); // in the console screen we will see 5, although the add variable is declared in the next line of code
var add;

==============================================================================================================================

const person = {
    firstName: 'John', // property of type string
    lastName: 'Smith',
    'middleName': 'Adam', // the key can be saved as a string
    grades: [4, 6, 5], // property being an array
    job: { // property being an object
        position: 'Software Developer',
        mainLanguage: 'Not JavaScript'
    },
    describeJob: function () { // the function is also an object property (the so-called method)
        console.log(`${this.firstName} has job ${this.job.position} and main language is ${this.job.mainLanguage}`);
    },
    welcome: () => console.log('hi ' + this.firstName) // the arrow function can also be an object property
};

console.log(person.firstName); // John / a dotted notation was used
console.log(person['lastName']); // Smith / a bracketed notation was used
console.log(person.middleName); // Adam
person.describeJob(); // calling the method on the object
person.welcome(); // hi undefined 

function createAnimal(name) {
    return {
        name, // the abbreviated notation explained below
        type: `dog`
    }
}

const animal = createAnimal('Kitty');
console.log(animal); // will be displayed {name: "Kitty",type: "dog"}

const person = new Object(); // alternative for { }
person.firstName = "John";
person.lastName = "Doe";

console.log(person); // {firstName:"John",lastName:"Doe"} will be displayed

function Person(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.describe = () => console.log(`${this.firstName} ${this.lastName} has age ${this.age}`);
}

const person = new Person("John", "Doe", 7);
person.describe();

class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.allGrades = [];
    }

    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    }

    set grades(grade) {
        this.allGrades.push(grade);
    }

    getWelcomeMessage = () => `Hello ${this.firstName}`;
}

const person = new Person('Andrew', 'Williams'); // creating an object defined with class
console.log(person.getWelcomeMessage()); // Hello Andrew
console.log(person.fullName); // Andrew Williams
person.grades = 5;
person.grades = 6;
console.log(person.allGrades); // [5,6]

==============================================================================================================================
*/
// DOM Model
