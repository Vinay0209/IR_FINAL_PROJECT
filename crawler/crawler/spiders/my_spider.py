import scrapy


class MySpider(scrapy.Spider):
    name = "my_crawler"  # Name of your spider

    # Define starting URL, adjust as needed
    start_urls = ["https://quotes.toscrape.com/"]

    # Maximum pages to crawl (adjust the limit)
    max_pages = 100

    # Maximum depth to follow links (adjust the limit)
    max_depth = 10

    # Current page count (internal variable)
    page_count = 0

    def parse(self, response):
        # Check if page limit is reached
        if self.page_count >= self.max_pages:
            return

        # Extract HTML content (replace with your specific logic)
        html_content = response.css("body").get()  # Example using CSS selector

        # Save the HTML content (replace with your saving logic)
        filename = f"page_{self.page_count}.html"  # Example filename format
        with open(filename, "wb") as f:
            f.write(html_content.encode())

        self.page_count += 1

        # Follow links within the page (limited by depth)
        # Access depth from response.meta
        if response.meta.get('depth') < self.max_depth:
            for next_page in response.css("a::attr(href)").getall():
                if next_page.startswith("/"):  # Check for relative URLs
                    yield response.follow(next_page, callback=self.parse, meta={'depth': response.meta.get('depth', 0) + 1})

# Run the spider (replace with your command)
# scrapy crawl my_crawler -o scraped_data.json
