import scrapy

class Directory2Spider(scrapy.Spider):
    name = 'directory_2'
    allowed_domains = ['exhibitors.exporeal.net']
    start_urls = ['https://exhibitors.exporeal.net/ausstellerverzeichnis/2024/aussteller/']

    '''For exporting data as json'''
    # custom_settings = {
    #     "FEED_EXPORT_ENCODING" : "utf-8",
    # }

    def parse(self, response):
        items = response.css('div.pb_ce div.ct_le')
        for item in items:
            url = item.css('div.ce_cntnt div.ce_head h2 a::attr(href)').get()
            if url:
                yield response.follow(url, callback=self.parse_data)

        form_data = {
            "LNG": "1",
            "nv": '2',
            "rqt_spcListing": "allEx",
            "clgk": "",
            "sb_reset": "",
            "sb_sort": "abc",
            "sb_view": "ext",
            "sb_rpp": "15",
            "sb_c": "5",
            "sb_m": "1100",
            "sb_n": "mainSearch",
            "sb_s": "",
            "once_sb_additionalFields": "E_ParentCount",
            "sb1": "IS NOT NULL",
            "sb1_n": "suche",
            "sb1_t": "basic",
            "sb1_s": "",
            "sb2": "ex",
            "sb2_n": "bereiche",
            "sb2_t": "ignoreCondition",
            "sb2_s": "",
            "sb3": "TB",
            "sb3_n": "list2Not",
            "sb3_t": "listItem",
            "sb3_s": "not",
            "sb4": "",
            "sb4_n": "abc",
            "sb4_t": "",
            "sb4_s": "LEFT",
            "sb5": "",
            "sb5_n": "tabs",
            "sb5_t": "",
            "sb5_s": "",
            "SRFieldtext": "",
            "SRField_next": "next",
            "StartRow_query_res_first": response.xpath('//input[@name="StartRow_query_res_first"]/@value').get(),
            "StartRow_query_res_previous": response.xpath('//input[@name="StartRow_query_res_previous"]/@value').get(),
            "StartRow_query_res_next": response.xpath('//input[@name="StartRow_query_res_next"]/@value').get(),
            "StartRow_query_res_last": response.xpath('//input[@name="StartRow_query_res_last"]/@value').get(),
            "StartRow_query_res_nextSet": response.xpath('//input[@name="StartRow_query_res_nextSet"]/@value').get(),
            "StartRow_query_res_previousSet": response.xpath('//input[@name="StartRow_query_res_previousSet"]/@value').get(),
            "StartRow_query_res_lazyLoadMore": response.xpath('//input[@name="StartRow_query_res_lazyLoadMore"]/@value').get(),
            "StartRow_query_res_lazyLoadLess": response.xpath('//input[@name="StartRow_query_res_lazyLoadLess"]/@value').get(),
            "Previous_PageNumber_query_res": response.xpath('//input[@name="Previous_PageNumber_query_res"]/@value').get(),
            "rqt_pagingQuery": "query_res",
            "rqt_pagingDef": "15",
        }
        
        yield scrapy.FormRequest(
                url='https://exhibitors.exporeal.net/ausstellerverzeichnis/2024/aussteller/',
                formdata=form_data,
                callback=self.parse,
                method='POST'
            )


    def parse_data(self, response):
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