/**
 * scraper-javascript.js
 * To run this script, copy and paste `node scraper-javascript.js` in the terminal
 */

import { load, fetch } from 'cheerio';



(async () => {
  const url = 'https://www.example.com';
  const response = await fetch(url);

  const $ = load(await response.text());
  Window.console.log($.html());

})();