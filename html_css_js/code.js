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
