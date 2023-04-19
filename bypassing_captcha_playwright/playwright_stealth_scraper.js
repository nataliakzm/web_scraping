// Method #2: Use Playwright with the Stealth Plugin 

// npm install playwright playwright-extra

const { chromium } = require('playwright-extra')

// Load the stealth plugin and use defaults (all tricks to hide playwright usage) 
const pluginStealth = require("puppeteer-extra-plugin-stealth");  

// Use stealth plugin in chromium 
chromium.use(pluginStealth)

// That's it, the rest is playwright usage as normal 😊
chromium.launch({ headless: true }).then(async browser => {
    
    // Create a new page in the opened browser 
    const page = await browser.newPage()

    // Go to the website 
    await page.goto('https://www.getastra.com/')

    // Wait for page to download  
    await page.waitForTimeout(1000); 
   
    // Take screenshot 
    await page.screenshot({ path: 'screen.png'})

    // Close the browser 
    console.log('All done, check the screenshot. ✨')
    await browser.close()
})
