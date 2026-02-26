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

  valid = validatePassword();
  if (!valid) {
    const passwordError = document.querySelector("#password + span");
    passwordError.style = "visibility: visible";
    passwordError.innerText = "Invalid password";
    validForm = false;
  }

  valid = validateEmail();
  if (!valid) {
    const emailError = document.querySelector("#email + span");
    emailError.style = "visibility: visible";
    emailError.innerText = "Invalid email";
    validForm = false;
  }
  valid = validateAge();
  if (!valid) {
    const ageError = document.querySelector("#age + span");
    ageError.style = "visibility: visible";
    ageError.innerText = "Invalid age";
    validForm = false;
  }
  valid = validateActivationDate();
  if (!valid) {
    const activationDateError = document.querySelector(
      "#activationDate + span",
    );
    activationDateError.style = "visibility: visible";
    activationDateError.innerText = "Incorrect activation date";
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

function validatePassword() {
  const password = document.getElementById("password")["value"];
  if (password == null) return false;
  if (password.length < 3 || password.length > 12) return false;
  const pattern = new RegExp(".*[!@#$%].*");
  if (!pattern.test(password)) return false;
  return true;
}

function validateEmail() {
  const email = document.getElementById("email")["value"];
  if (email == null) return false;
  const pattern = new RegExp(
    `(?:[a-z0-9!#$%&'*+/=?^_\`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_\`{|}~-]+)*|"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+))\\]`,
  );
  if (!pattern.test(email)) return false;
  return true;
}

function validateAge() {
  const age = document.getElementById("age")["value"];
  if (age == null) return false;
  if (age == "") return false;
  if (age < 0 || age > 122) return false;
  return true;
}

function validateActivationDate() {
  const activationDateText = document.getElementById("activationDate")["value"];
  if (activationDateText == null) return false;
  if (activationDateText == "") return false;
  const activationDate = new Date(activationDateText);
  const now = new Date();
  now.setHours(0, 0, 0, 0);
  if (activationDate.getTime() < now.getTime()) return false;
  const sevenDaysFromNow = new Date(now.getTime() + 1000 * 60 * 60 * 24 * 7);
  activationDate.setHours(0, 0, 0, 0);
  if (activationDate.getTime() > sevenDaysFromNow.getTime()) return false;
  return true;
}
