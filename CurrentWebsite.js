function onGot(page) {
  page.foo();
}

function onError(error) {
  console.log(`Error: ${error}`);
}

var getting = browser.runtime.getBackgroundPage();
document.getElementById("tester").innerText = "Website"+getting
getting.then(onGot, onError);