function validateForm() {
  // To start working with the form, we specify that it is correct by default
  // and hide the resulting message until the form is checked at the end
  let validForm = true;
  const formResult = document.getElementById("form-result");
  formResult.style = "display: none";

  // By default, we clear all error messages and set them as
  // "invisible"
  const errorMsgs = document.querySelectorAll("form p span");
  errorMsgs.forEach(function (errorMsg) {
    errorMsg.style = "visibility: hidden";
    errorMsg.innerText = "";
  });

  // We repeat this procedure for each field:
  // - we validate with a dedicated function
  // - if the field is invalid, we find the span after that field
  // - we set the visibility of this element
  // - we add some error inside this element
  // - we define the entire form as invalid
  let valid = validateUsername();
  if (!valid) {
    const usernameError = document.querySelector("#username + span");
    usernameError.style = "visibility: visible";
    usernameError.innerText = "Invalid username";
    validForm = false;
  }

  formResult.style = "display: block";
  if (validForm) {
    formResult.innerText = "The form was completed without errors!";
  } else {
    formResult.innerText = "Fix all errors!";
  }
}

function validateUsername() {
  // We get an element with id username and the value of its value attribute
  const username = document.getElementById("username")["value"];
  // We check if the value has been defined
  if (username == null) return false;
  // We check that the value is not shorter than 3
  if (username.length < 3) return false;

  // We create a regular expression to test
  const pattern = new RegExp("^[-_.a-z]+$");
  // We check if the text entered in the username field meets the assumptions of the regular expression
  if (!pattern.test(username)) return false;
  return true;
}
