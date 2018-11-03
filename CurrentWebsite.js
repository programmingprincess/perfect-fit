function foo() {
	var gettingCurrent = browser.tabs.getCurrent();
	console.log(gettingCurrent.url);
}
