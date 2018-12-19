function handleResponse(message) {
  console.log(`Message from the background script:  ${message.response}`);
}

function handleError(error) {
  console.log(`Error: ${error}`);
}

function listeners() {
  console.log("listener")
  document.getElementById("options").addEventListener('click', notifyBackground);
  var lol = document.getElementById("options")
  console.log(lol)
}

function notifyBackground(e) {
  console.log("notifyBackground")
  var lol = document.getElementById("options")
  console.log(lol)
  var sending = browser.runtime.sendMessage({
    greeting: "Open Options"
  });
  sending.then(handleResponse, handleError);  
}

function getPage() {
	browser.tabs.query({currentWindow: true, active: true})
		.then((tabs) => {
      var host = getHostName(tabs[0].url)
      if(host.length > 0) {
        document.getElementById("current_store").textContent = host;
      } else {
        document.getElementById("current_store").textContent = "no url";
      }
	})
}

function getStorage() {
  function setCurrentChoices(result) {
    document.getElementById("saved_store").textContent = result.store;
    document.getElementById("saved_topSize").textContent = result.topSize;
    document.getElementById("saved_botSize").textContent = result.botSize;
    //document.getElementById("default-store").textContent = result.store || "Abercrombie";
  }

  function onError(error) {
    console.log(`Error: ${error}`);
  }

  var getting = browser.storage.sync.get(["store", "topSize", "botSize"])
  getting.then(setCurrentChoices, onError);
}

function getHostName(url) {
  // var matches = url.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i);
  // var domain = matches && matches[1];  // domain will be null if no match is found
  var match = url.match(/:\/\/(www[0-9]?\.)?(.[^/:]+)/i);
  if (match != null && match.length > 2 && typeof match[2] === 'string' && match[2].length > 0) {
    return match[2]
  }
  else {
    return "";
  }
}

listeners();
getPage();
getStorage();
