import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DirectorySpider(CrawlSpider):
    name = "directory"
    allowed_domains = ["exhibitors.exporeal.net"]
    start_urls = ["https://exhibitors.exporeal.net/ausstellerverzeichnis/2024/branchen/"]

    rules = (
        Rule(LinkExtractor(restrict_css="a.btTsAr") , follow=True),
        Rule(LinkExtractor(restrict_css="div.ce_head h2>a"), callback="parse_item", follow=True),
        )

    def parse_item(self, response):

        Title = response.css('div.ce_cntct > div.ce_head ::text').get().strip()
        Address = response.css('div.ce_addr ::text').get().strip()
        Phone = response.xpath('//div[@class="ce_cTxt"]/a[@title="Telefon"]/text()').get()
        Mobile = response.xpath('//div[@class="ce_cTxt"]/a[@title="Mobil"]/text()').get()
        Email = response.xpath('//div[@class="ce_cTxt"]/a[@title="E-Mail"]/text()').getall()
        Website = response.css('div.ce_website > a::attr(href)').getall()
        Linkedin = response.css('div.ce_smch.ce_LinkedIn > a::attr(href)').get()

        yield{
            'Title' : Title,
            'Address' : Address,
            'Phone' : Phone,
            'Mobile' : Mobile,
            'Email' : Email,
            'Website' : Website,
            'LinkeIn' : Linkedin,
            'URL' : response.url
        }
