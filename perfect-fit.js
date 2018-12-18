document.body.style.border = "5px solid blue";

function getPage() {
	browser.tabs.query({currentWindow: true, active: true})
		.then((tabs) => {
			console.log(tabs[0].url);
	})
}

function getStorage() {
	var storageitem = browser.storage.local.get('store');
	var default_store = document.getElementById("default_store");
  var newStore = "";
  storageitem.then((res) => {
  	newStore = `${res.store}`;
    console.log(`popup selected store: ${res.store}`);
  });
  default_store.textContent = newStore;
  debugger
  document.getElementById("tester").innerText = "hey testing this is working";
}

document.querySelector("form").addEventListener("submit", getStorage);
getPage();
