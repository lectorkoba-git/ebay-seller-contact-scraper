# 💼 eBay Seller Contact Scraper: B2B Email, Phone & Company Info

[![eBay Seller Contact Scraper](https://apify.com/actor-badge?actor=magic-scraper/ebay-seller-contact-scraper)](https://apify.com/magic-scraper/ebay-seller-contact-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$10%20%2F%201K%20results-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Python, Node.js and REST examples for the **[eBay Seller Contact Scraper](https://apify.com/magic-scraper/ebay-seller-contact-scraper)** on Apify: the legally required business seller disclosure of an eBay listing — company name, address, phone, email, feedback score and store URL — by item ID or listing URL.

> ⚡ **No code needed:** 👉 **[Run it in your browser on Apify (free $5 monthly credit)](https://apify.com/magic-scraper/ebay-seller-contact-scraper)**

---

## 🎯 Who is this for?

- **B2B lead generation** — build outreach lists of active business sellers.
- **Dropshippers & wholesale scouts** — find and contact suppliers behind listings.
- **Brand protection** — identify the legal entity behind unauthorized or counterfeit listings.
- **CRM enrichment** — turn item IDs from your own pipeline into company contacts.

---

## 📌 Key Facts

| | |
| :--- | :--- |
| **Pricing** | $10.00 per 1,000 seller contacts ($0.01 per result) + $0.00005 start fee; ≈500 contacts/month inside Apify's free $5 credit |
| **Not found = not charged** | Ended, removed or unavailable items are skipped (listed in the run's `OUTPUT` record) and never charged |
| **Run time (measured)** | ~4–8 s for a 2-item run; items fetched in parallel (`poolCount` up to 30) |
| **How it works** | Plain HTTP with browser TLS impersonation and server-rendered page data, ~50–80 MB memory, no headless browser |
| **Blocked requests** | A blocked IP is swapped for a fresh proxy session and the item is retried (up to 3 attempts) |
| **Login / cookies** | Not required |

### ⚠️ Limitations

- Contacts exist only for **business sellers** — eBay does not publish them for private sellers.
- During eBay-wide anti-bot waves most requests can be challenged for a while; affected items are not saved and not charged — re-run later.

---

## 🚀 Quickstart

### Python

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("magic-scraper/ebay-seller-contact-scraper").call(run_input={
    "itemIds": ["318445065346", "https://www.ebay.com/itm/253995891196"],
    "poolCount": 10,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    s = item["seller"]
    print(item["item_id"], s["companyName"], s["email"], s["phone"])
```

### Node.js

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('magic-scraper/ebay-seller-contact-scraper').call({
    itemIds: ['318445065346', '253995891196'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (synchronous run, returns the dataset)

```bash
curl -X POST "https://api.apify.com/v2/acts/magic-scraper~ebay-seller-contact-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"itemIds": ["318445065346"]}'
```

---

## 📥 Input

| Parameter | Type | Default | Description |
| :--- | :--- | :---: | :--- |
| `itemIds` | `array` | required | Item IDs (`318445065346`), listing URLs, or `{"item_id": "..."}` objects. |
| `poolCount` | `integer` | `10` | Parallel workers (1–30). |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true}` | Apify Proxy (Datacenter by default, Residential optional). |

---

## 📤 Output

One record per item where a business seller disclosure was found:

| Field | Type | Description |
| :--- | :--- | :--- |
| `item_id` | `string` | eBay item ID. |
| `url` | `string` | Listing URL. |
| `seller.seller` | `string` | eBay username / contact name. |
| `seller.companyName` | `string \| null` | Registered business name. |
| `seller.address` | `string \| null` | Business address. |
| `seller.phone` | `string \| null` | Business phone. |
| `seller.email` | `string \| null` | Business email. |
| `seller.feedbackScore` | `integer \| null` | Feedback score. |
| `seller.positiveFeedbackPercent` | `number \| null` | Positive feedback %. |
| `seller.storeUrl` | `string \| null` | eBay store URL. |

### Sample record (real run)

```json
{
  "item_id": "318445065346",
  "url": "https://www.ebay.com/itm/318445065346",
  "seller": {
    "seller": "autoboost2024",
    "companyName": "Shifang Innovation Co   Limited",
    "address": "Room D,10/F,Unionway Commercial Centre, 283 Queens Road Central,Sheung Wan, Hong Kong, 999077, Hong Kong",
    "phone": "+86 13802292205",
    "email": "autoboost24@outlook.com",
    "feedbackScore": 3508,
    "positiveFeedbackPercent": 99.5,
    "storeUrl": "https://www.ebay.com/str/autoboost2024"
  }
}
```

---

## 🤖 For AI Agents

Call `magic-scraper/ebay-seller-contact-scraper` via the [Apify MCP server](https://mcp.apify.com/) or the API with `{"itemIds": ["<id or URL>"]}`. Only found sellers are returned (and charged); keep `poolCount` ≤ 30.

---

## ⚖️ Legal

The actor reads only the business seller information eBay publishes on listing pages under seller-transparency rules (US INFORM Consumers Act, EU and UK consumer law). It does not log in or access private data. You are responsible for complying with GDPR, CAN-SPAM and other laws when contacting sellers.

---

## 🔗 Related Scrapers

- [Etsy Bestsellers & Tags Scraper](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper)
- [Temu Trending Products & Lightning Deals Tracker](https://apify.com/magic-scraper/temu-trending-products-scraper)
- [TikTok Shop Search Scraper](https://apify.com/magic-scraper/tiktok-shop-search-scraper)

---

## 📄 License

MIT — see [LICENSE](LICENSE). This repository contains usage examples; the scraper itself runs on [Apify](https://apify.com/magic-scraper/ebay-seller-contact-scraper).
