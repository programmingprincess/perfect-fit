document.body.style.border = "5px solid red";

function getPage() {
	browser.tabs.query({currentWindow: true, active: true})
		.then((tabs) => {
			console.log(tabs[0].url);
	})
}

getPage();
