# 💼 eBay Seller Contact Scraper: B2B Email, Phone & Legal Company Info

[![eBay Seller Contact Scraper](https://apify.com/actor-badge?actor=magic-scraper/ebay-seller-contact-scraper)](https://apify.com/magic-scraper/ebay-seller-contact-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![High Speed](https://img.shields.io/badge/Speed-~0.3s%20per%20item-brightgreen?style=flat-square)
![Data](https://img.shields.io/badge/Data-Verified%20B2B%20Contacts-blue?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Extract verified **eBay seller B2B contact details** directly by Item ID or listing URL: legal company name, direct business email, phone number, physical registered address, seller feedback score, positive feedback rate, and store URL at high speed.

> ⚡ **Try it directly in your browser without code:**  
> 👉 **[Run eBay Seller Contact Scraper on Apify (Free $5 Monthly Credits)](https://apify.com/magic-scraper/ebay-seller-contact-scraper)**

---

## 🎯 Who is this for?

- **B2B Lead Generation Agencies:** Build targeted outreach lists of high-volume active merchants.
- **Dropshippers & Wholesale Scouts:** Locate reliable product suppliers and negotiate direct contracts outside platform fees.
- **Amazon & Shopify Arbitrage Sellers:** Source manufacturer contacts from trending eBay product listings.
- **Market Researchers & Brand Protection:** Audit counterfeit products or unauthorized distributors using legal business disclosures.

---

## ⚡ Why Choose This Extractor Over Legacy Scrapers?

| Feature | **Our eBay Extractor** | Legacy Playwright Scrapers |
| :--- | :---: | :---: |
| **Speed (50 items)** | ⚡ **~7 seconds** | 🐢 2–5 minutes |
| **Direct Contact Info** | ✅ **Direct business email & phone included** | ❌ Missing or username only |
| **Company Legal Name** | ✅ Registered corporate entity name | ❌ Missing |
| **Physical Address** | ✅ Full legal business address | ❌ Hidden behind clicks |
| **Zero Browser Overhead** | ✅ Native TLS requests (<60 MB RAM) | ❌ Heavy Chromium crashes (3 GB image) |
| **Timeout Resilience** | ✅ Handles ended/404 items in 0.1s | ❌ 25s `Page.goto` timeout crashes |
| **Input Flexibility** | ✅ Accepts IDs, URLs, or structured objects | ❌ Strict single string format |

---

## 📖 How to Extract eBay Seller Contacts (Step-by-Step)

1. **Enter Item IDs or URLs:** Provide eBay Item IDs (e.g. `318445065346`), listing URLs (`https://www.ebay.com/itm/318445065346`), or an array of objects.
2. **Set Concurrency:** (Optional) Adjust `poolCount` (default: `10`, up to `30` parallel workers).
3. **Run & Export:** Click **Start**. Once finished, export your enriched B2B dataset to **CSV, Excel, JSON, Google Sheets**, or integrate directly via API.

---

## 📥 Input Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `itemIds` | `array[string]` | **Yes** | `["318445065346"]` | Array of eBay item IDs, listing URLs, or objects. |
| `poolCount` | `integer` | No | `10` | Concurrency worker count processing items in parallel (1–30). |
| `proxyConfiguration` | `object` | No | Datacenter | Proxy settings. Supports Apify Datacenter or Residential proxy. |

---

## 📤 Sample Output (JSON)

```json
{
  "item_id": "277961689107",
  "url": "https://www.ebay.com/itm/277961689107",
  "seller": {
    "seller": "Antonakis Antoniou",
    "companyName": "A.A XPRES SALES LLC",
    "address": "16192 Coastal Hwy, Lewes, DE, 19958, United States",
    "phone": "+357 99890980",
    "email": "antonis1681@gmail.com",
    "feedbackScore": 5521,
    "positiveFeedbackPercent": 99.5,
    "storeUrl": "https://www.ebay.com/str/xpressalesstore"
  }
}
```

---

## 💻 Developer Quickstart (Python & Node.js)

### Python (`apify-client`)

```bash
pip install apify-client
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))

run_input = {
    "itemIds": ["318445065346", "253995891196", "156345471674"],
    "poolCount": 10
}

run = client.actor("magic-scraper/ebay-seller-contact-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    seller = item.get("seller", {})
    print(f"Merchant: {seller.get('companyName')} | Email: {seller.get('email')} | Phone: {seller.get('phone')}")
```

### Node.js (`apify-client`)

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({
    token: process.env.APIFY_TOKEN || 'YOUR_APIFY_TOKEN',
});

const run = await client.actor('magic-scraper/ebay-seller-contact-scraper').call({
    itemIds: ['318445065346', '253995891196'],
    poolCount: 10,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (REST API)

```bash
curl "https://api.apify.com/v2/acts/magic-scraper~ebay-seller-contact-scraper/runs?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"itemIds": ["318445065346"]}'
```

---

## 💳 Pricing & Free Tier ($5 Monthly Credit)

This Actor runs on Apify's serverless infrastructure:
- **Apify Free Plan:** You receive **$5.00 in free usage credits every month**.
- **Ultra-lightweight compute:** Because this actor uses native HTTP SSR requests instead of heavy headless browsers, 1,000 items consume only a fraction of compute units.
- **Zero Risk:** You can scrape hundreds of sellers completely free before paying anything.

👉 **[Start Scraping Free on Apify](https://apify.com/magic-scraper/ebay-seller-contact-scraper)**

---

## ⚖️ Legal & GDPR Compliance

This Actor extracts only publicly available commercial seller disclosures that merchants are legally required to display under consumer protection laws (EU/UK/US commercial seller disclosures). It does not access private accounts, bypass passwords, or scrape protected consumer data. Always comply with relevant data protection legislation (GDPR, CCPA) when handling business contact information.
