/** Optional live browser check:
 *  python -m streamlit run app.py --server.headless true
 *  npm install --no-save --package-lock=false playwright
 *  npx playwright install chromium
 *  node tests/browser-check.cjs
 *  Or use a system Chrome via PLAYWRIGHT_CHANNEL=chrome.
 */
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');

(async () => {
  const browser = await chromium.launch({ channel: process.env.PLAYWRIGHT_CHANNEL || undefined });
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const checkFooter = async () => {
    const footer = page.locator('.st-key-contact_footer');
    await footer.waitFor();
    for (const [name, url] of [
      ['GitHub', 'https://github.com/Ycany-Sanchez'],
      ['LinkedIn', 'https://www.linkedin.com/in/ycany-ashra-sanchez-bb987937a/'],
    ]) {
      assert.equal(await page.getByRole('link', { name, exact: true }).count(), 1);
      assert.equal(await footer.getByRole('link', { name, exact: true }).getAttribute('href'), url);
    }
    assert.equal(await page.getByTestId('stSidebar').getByRole('radio', { name: 'Contact', exact: true }).count(), 0);
    assert.equal(await page.getByRole('textbox').count(), 0);
    assert.equal(await page.getByRole('combobox').count(), 0);
    assert.equal(await page.getByRole('button', { name: /download/i }).count(), 0);
  };
  const navigate = async section => {
    await page.getByTestId('stSidebar').getByRole('radio', { name: section, exact: true }).check();
    if (section === 'About') {
      await page.getByRole('button', { name: 'View projects', exact: true }).waitFor();
    } else {
      await page.getByRole('heading', { name: section, exact: true }).waitFor();
    }
    await checkFooter();
  };
  try {
    await page.goto(process.env.PORTFOLIO_URL || 'http://localhost:8501');
    await page.getByRole('heading', { name: 'Ycany Ashra T. Sanchez', exact: true }).waitFor();
    await page.getByRole('button', { name: 'View projects', exact: true }).waitFor();
    await checkFooter();
    fs.mkdirSync('artifacts', { recursive: true });
    await page.screenshot({ path: 'artifacts/about-desktop.png', fullPage: true });

    await navigate('Projects');
    for (const name of ['Parola', 'BantAI Buddy', 'IMentia', 'FoodPantry']) {
      await page.getByRole('heading', { name, exact: true }).waitFor();
    }
    await page.waitForFunction(() => {
      const images = [...document.querySelectorAll('[data-testid="stImage"] img')];
      return images.length === 3 && images.every(image => image.complete && image.naturalWidth > 0);
    });
    const tables = page.getByRole('table');
    assert.ok(await tables.count() > 0);
    assert.ok((await tables.allTextContents()).some(text => text.includes('Top 25 qualifier') && text.includes('Central Visayas')));
    assert.ok((await tables.allTextContents()).some(text => text.includes('Best Logo') && text.includes('Central Visayas')));

    await navigate('Skills');
    await page.getByRole('table').waitFor();
    assert.equal(await page.getByRole('slider').count(), 0);
    assert.equal(await page.getByTestId('stForm').count(), 0);

    await navigate('About');
    await page.setViewportSize({ width: 390, height: 844 });
    const closeSidebar = page.getByRole('button', { name: /close sidebar/i });
    if (await closeSidebar.isVisible()) await closeSidebar.click();
    await page.screenshot({ path: 'artifacts/about-mobile.png', fullPage: true });
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), 'No horizontal overflow');
    assert.deepEqual(errors, []);
    console.log('Browser checks passed. Screenshots are in artifacts/.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
