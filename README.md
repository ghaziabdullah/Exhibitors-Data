# Project Overview

The data is scrapped from the target website using two different approaches:

## 1. CrawlSpider
The spider crawls the site and scrapes data by going 4 levels deep. This approach is useful for extracting data that spreads across multiple linked pages.

## 2. Scrapy Spider
The data is also available on a single level, which is scraped using a simpler Scrapy Spider. This method is more straightforward.

## Handling Pagination
The tricky part of this project is managing pagination. The "Next Page" button does not link to a simple URL; instead, it sends a `POST` request, which requires specific form data to be included with the request.
