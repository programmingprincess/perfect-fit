function saveOptions(e) {

  var topSize = document.getElementById("topInput").value;
  document.getElementById("top-size").textContent = topSize;

  var bottomSize = document.getElementById("bottomInput").value;
  document.getElementById("bottom-size").textContent = bottomSize;

  console.log(document.getElementById("store-list").value);

  browser.storage.local.set({
    store: document.querySelector("#store-list").value,
    topSize: topSize
  });

  var storageitem = browser.storage.local.get('store');
  storageitem.then((res) => {
    console.log(`stored store is: ${res.store}`);
  });

  storageitem = browser.storage.local.get('topSize');
  storageitem.then((res) => {
    console.log(`stored topSize is: ${res.topSize}`);
  });

  e.preventDefault();
}

function restoreOptions() {
  var stores = list_of_stores.stores;
  stores.sort();
  var options = "";

  for(var store in stores) {
    options += '<option value="' + stores[store] + '">' + stores[store] + '</option>'
  }

  document.getElementById("store-list").innerHTML = options;

  var savedStore = "";

  var storedStore = browser.storage.local.get("store");
  storedStore.then((res)=> {
    savedStore = `${res.store}`;
  })

  var savedTopSize= "";
  var storedTop = browser.storage.local.get("topSize");
  storedTop.then((res)=> {
    savedTopSize = `${res.topSize}`;
    console.log("dom has been reloaded, update new top size now!");
  })

  document.getElementById("top-size").textContent = savedTopSize;

}

document.addEventListener('DOMContentLoaded', restoreOptions);
document.querySelector("form").addEventListener("submit", saveOptions);

