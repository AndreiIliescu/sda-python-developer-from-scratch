/*
// 1. Create a new XMLHttpRequest object
let xhr = new XMLHttpRequest();

// 2. Configure it: GET-request for the URL /article/.../load
xhr.open("GET", "https://jsonplaceholder.typicode.com/posts/1");

// 3. Send the request over the network
xhr.send();

// 4. This will be called after the response is received
xhr.onload = function () {
  if (xhr.status != 200) {
    // analyze HTTP status of the response
    alert(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
  } else {
    // show the result
    alert(`Done, got ${xhr.response.length} bytes`); // response is the server
  }
};

xhr.onprogress = function (event) {
  if (event.lengthComputable) {
    alert(`Received ${event.loaded} of ${event.total} bytes`);
  } else {
    alert(`Received ${event.loaded} bytes`); // no Content-Length
  }
};

xhr.onerror = function () {
  alert("Request failed");
};

===============================================================================================================================
*/

fetch("https://restcountries.eu/rest/v2/name/Poland")
  .then((res) => res.json()) // received data convert to the JSON format
  .then((res) => {
    // definition of what to do
    console.log(res);
  });

fetch("...", {
  method: "POST", //*GET, POST, PUT, DELETE, etc.
  mode: "cors", //no-cors, *cors, same-origin
  cache: "no-cache", //*default, no-cache, reload, force-cache, only-if-cached
  credentials: "same-origin", //include, *same-origin, omit
  headers: {
    "Content-Type": "application/json",
    // 'Content-Type': 'application/x-www-form-urlencoded',
  },
  redirect: "follow", // manual, *follow, error
  referrerPolicy: "no-referrer", // no-referrer, *client
  body: JSON.stringify(data), //treść wysyłana
});
