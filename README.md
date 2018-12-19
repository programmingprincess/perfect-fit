# Perfect Fit
Matching size charts for online shopping

## Our API
Access to our webscraped data can be found [here](https://heabuh.com/perfectfit/)

## Notes 

We are now using `browser.storage.sync` instead of local storage, but the storage file will be kept in the repo.

`perfect-fit@mozilla.org.json` needs to be placed in `~/Library/Application Support/Mozilla/ManagedStorage` in order to save user size information throughout multiple sessions. 

## TODO

Functionality 
- [ ] Integrate front-end and back-end 
- [ ] Settle ambiguity between "tops" vs. "shirts" vs. "sweaters" (store naming conventions)
- [x] Open up options page from extension popup 
- [ ] Display domain name or store name? (If the latter, we may need to create a dictionary to map domains to store names)


Features 
- [ ] UI design
- [ ] Allow users to select bust/waist preference for tops 
- [ ] Auto-calculate bust/waist/hip sizes based on numeric/letter size (i.e., given S, calculate Bust = 32 and Waist = 24...)
- [ ] Men's sizing 
- [ ] Also have a website that does calculations? 
- [ ] Tooltip when hovering over calculated sizes to explain calculations?

## Awards 

Judge's Pick at [CodeAda 2018](https://www.facebook.com/events/2104844719580256/), University of Illinois! (November, 2018)
