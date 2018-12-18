function saveOptions(e) {
  e.preventDefault();

  browser.storage.sync.set({
    store: document.querySelector("#store-list").value,
    topSize: document.getElementById("topInput").value,
    botSize: document.getElementById("bottomInput").value
  })
  console.log("Saved options")
}

function restoreOptions() {
  var stores = list_of_stores.stores;
  stores.sort();
  var options = "";

  for(var store in stores) {
    options += '<option value="' + stores[store] + '">' + stores[store] + '</option>'
  }

  document.getElementById("store-list").innerHTML = options;
  function setCurrentChoices(result) {
    document.getElementById("selected-store").textContent = result.store || "Abercrombie";
    document.getElementById("top-size").textContent = result.topSize || "M";
    document.getElementById("bottom-size").textContent = result.botSize || "29";
  }

  function onError(error) {
    console.log(`Error: ${error}`);
  }

  var getting = browser.storage.sync.get(["store", "topSize", "botSize"])
  getting.then(setCurrentChoices, onError);

}

document.addEventListener('DOMContentLoaded', restoreOptions);
document.querySelector("form").addEventListener("submit", saveOptions);

