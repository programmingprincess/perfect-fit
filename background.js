function handleClick() {
  //browser.runtime.openOptionsPage();
}

//browser.browserAction.onClicked.addListener(handleClick);

function handleMessage(request, sender, sendResponse) {
  browser.runtime.openOptionsPage();
  console.log("Message from the content script: " +
    request.greeting);
  if (request.greeting == "Open Options") {
  	browser.runtime.openOptionsPage();
  }
  sendResponse({response: "Opened options"});
}

browser.runtime.onMessage.addListener(handleMessage);