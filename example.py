"""
Example: Extract verified B2B contacts for eBay sellers via Apify Python Client.
Requires: pip install apify-client
"""
import os
from apify_client import ApifyClient

# Replace with your Apify API Token or set APIFY_TOKEN environment variable
APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    # Provide eBay Item IDs or listing URLs
    "itemIds": [
        "318445065346",
        "277961689107",
        "https://www.ebay.com/itm/253995891196"
    ],
    "poolCount": 10
}

print("🚀 Launching eBay Seller Contact Scraper on Apify Cloud...")
run = client.actor("magic-scraper/ebay-seller-contact-scraper").call(run_input=run_input)

print(f"✅ Run finished with status: {run.get('status')}")
print("📊 Extracted B2B Seller Contacts:\n")

dataset_id = run["defaultDatasetId"]
for item in client.dataset(dataset_id).iterate_items():
    seller = item.get("seller", {})
    print(f"Item ID: {item.get('item_id')}")
    print(f"  Seller:  {seller.get('seller')}")
    print(f"  Company: {seller.get('companyName')}")
    print(f"  Email:   {seller.get('email')}")
    print(f"  Phone:   {seller.get('phone')}")
    print(f"  Address: {seller.get('address')}")
    print(f"  Score:   {seller.get('feedbackScore')} ({seller.get('positiveFeedbackPercent')}%)\n")
