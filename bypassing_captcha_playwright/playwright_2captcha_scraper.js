// Method #1: Bypass CAPTCHA with Base Playwright and 2Captcha API (Recommended)

// npm install playwright
// npm install 2captcha

// Start with calling both Playwright and 2captcha API modules in your script
const { chromium } = require('playwright');
const Captcha = require("2captcha");

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

// Insert your API key here (you can get it from 2captcha.com)
const solver = new Captcha.Solver("<Your 2Captcha API key>");

// Call ReCaptcha Website URL here
const websiteUrl = "https://patrickhlauke.github.io/recaptcha/";
await page.goto(websiteUrl);

// Wait for the CAPTCHA element to load on the page (you can use any selector you want)
const captchaFrame = await page.waitForSelector("iframe[src*='recaptcha/api2']");

// Switch to the CAPTCHA iframe to interact with it 
const captchaFrameContent = await captchaFrame.contentFrame();

// Wait for the CAPTCHA checkbox to appear on the page 
const captchaCheckbox = await captchaFrameContent.waitForSelector("#recaptcha-anchor");

// Click the CAPTCHA checkbox to trigger the challenge 
await captchaCheckbox.click();

 // Wait for the CAPTCHA challenge to be solved by 2Captcha API 
 const captchaResponse = await solver.recaptcha("6Ld2sf4SAAAAAKSgzs0Q13IZhY02Pyo31S2jgOB5", websiteUrl);

 // Fill in the CAPTCHA response and submit the form
 const captchaInput = await captchaFrameContent.waitForSelector("#g-recaptcha-response");
 await captchaInput.evaluate((input, captchaResponse) => {
   input.value = captchaResponse;
 }, captchaResponse);
 await captchaFrameContent.waitForSelector("button[type='submit']").then((button) => button.click());

 // Wait for the page to navigate to the next page after the CAPTCHA is solved 
 await page.waitForNavigation();

 console.log("CAPTCHA solved successfully!");

 await browser.close();
})();
