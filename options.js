function saveOptions(e) {

  var topSize = document.getElementById("topInput").value;
  document.getElementById("top-size").textContent = topSize;

  e.preventDefault();
}

function restoreOptions() {
  var stores = list_of_stores.stores;
  stores.sort();
  console.log(stores);
  var options = "";

  for(var store in stores) {
    options += "<option value=" + stores[store] + ">" + stores[store] + "</option>"
  }

  document.getElementById("store-list").innerHTML = options;
}

//from stackoverflow 
//https://stackoverflow.com/questions/2499567/how-to-make-a-json-call-to-a-url/2499647#2499647
function getJSONP(url, success) {

    var ud = '_' + +new Date,
        script = document.createElement('script'),
        head = document.getElementsByTagName('head')[0] 
               || document.documentElement;

    window[ud] = function(data) {
        head.removeChild(script);
        success && success(data);
    };

    script.src = url.replace('callback=?', 'callback=' + ud);
    head.appendChild(script);
    debugger

}

document.getElementById("top-size").textContent = 'lollll';

document.addEventListener('DOMContentLoaded', restoreOptions);
document.querySelector("form").addEventListener("submit", saveOptions);

