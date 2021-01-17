# -*- coding: utf-8 -*-
import scrapy
from ..items import LaptopScrapperItem


class AmazonSpiderSpider(scrapy.Spider):
    pgno = 2
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/s?hidden-keywords=B07RTYFS9S%7CB07RRQBC1S%7CB07W6H3FM3%7CB07XP981T8%7CB07S8VNK4T%7CB07XP853QP%7CB07W847VZY%7CB07XZFYQ18%7CB07W6H9YM9%7CB00007MC29%7CB07THDPBYB%7CB07S8PXB2X%7CB07TD8KKDY%7CB07TK254ZM%7CB07VPK4LM6%7CB07TC65VBS%7CB07YSVQG5N%7CB07ZT7H58N%7CB07FGHZ1XV&pf_rd_i=1375424031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=4a259b4b-d75e-411b-b0ab-88b84f73c558&pf_rd_r=YBEKSNJT5NMAKKYQP2Y0&pf_rd_s=merchandised-search-13&pf_rd_t=101&ref=nb_sb_noss']

    def parse(self, response):
        items=LaptopScrapperItem()
        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_price = response.css('.a-price-whole::text').extract()
        score_rating = response.css('.aok-align-bottom').css('::text').extract()
        total_rating = response.css('.a-size-small .a-size-base').css('::text').extract()

        items['product_name']=product_name
        items['product_price'] = product_price
        items['score_rating'] = score_rating
        items['total_rating'] = total_rating
        yield items

        next_page= 'https://www.amazon.in/s?page=2&hidden-keywords=B07RTYFS9S%7CB07RRQBC1S%7CB07W6H3FM3%7CB07XP981T8%7CB07S8VNK4T%7CB07XP853QP%7CB07W847VZY%7CB07XZFYQ18%7CB07W6H9YM9%7CB00007MC29%7CB07THDPBYB%7CB07S8PXB2X%7CB07TD8KKDY%7CB07TK254ZM%7CB07VPK4LM6%7CB07TC65VBS%7CB07YSVQG5N%7CB07ZT7H58N%7CB07FGHZ1XV&pf_rd_i=1375424031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=4a259b4b-d75e-411b-b0ab-88b84f73c558&pf_rd_r=YBEKSNJT5NMAKKYQP2Y0&pf_rd_s=merchandised-search-13&pf_rd_t=101&qid=1579694681&ref=sr_pg_2'
        if AmazonSpiderSpider.pgno<=2:
            AmazonSpiderSpider.pgno+=1
            yield scrapy.Request(next_page, callback=self.parse)
