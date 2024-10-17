import asyncio
import re

def parse_product(response):
    print(f"found product: {response.url}")

async def run():
    callbacks = {
        # any url that contains "/products/" is a product page
        re.compile(".+/products/.+"): parse_product
    }
    url_filter = UrlFilter(domain="nytimes.com", subdomain="store")
    async with Crawler(url_filter, callbacks=callbacks) as crawler:
        await crawler.run(["https://store.nytimes.com/"])

if __name__ == "__main__":
    asyncio.run(run())