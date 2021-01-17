# -*- coding: utf-8 -*-
import scrapy
from ..items import LaptopScrapperItem

class FlipkartSpiderSpider(scrapy.Spider):
    pgno=2
    name = 'flipkart_spider'
    start_urls = ['https://www.flipkart.com/laptops/pr?sid=6bo%2Fb5g&p%5B%5D=sort%3Dpopularity&p%5B%5D=facets.price_range.to%3D70000&p%5B%5D=facets.price_range.from%3D50000&otracker=clp_metro_expandable_5_10.metroExpandable.METRO_EXPANDABLE_%25E2%2582%25B950%252C000%2Bto%2B%25E2%2582%25B970%252C000_laptops-store_498d3f89-fa47-4e2a-bee1-6abdb3838038_DesktopSite_wp8&fm=neo%2Fmerchandising&iid=M_5617c17b-3f5e-4e77-8b78-bf4350031fa8_10.498d3f89-fa47-4e2a-bee1-6abdb3838038_DesktopSite&ppt=sp&ppn=sp&page=1']

    def parse(self, response):
        items = LaptopScrapperItem()
        product_name = response.css('div._3wU53n::text').extract()
        product_price = response.css('._2rQ-NK::text').extract()
        score_rating = response.css('.hGSR34::text').extract()
        total_rating = response.css('._38sUEc span span:nth-child(1)').css('::text').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['score_rating'] = score_rating
        items['total_rating'] = total_rating
        yield items

        next_page = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Fb5g&p%5B%5D=sort%3Dpopularity&p%5B%5D=facets.price_range.to%3D70000&p%5B%5D=facets.price_range.from%3D50000&otracker=clp_metro_expandable_5_10.metroExpandable.METRO_EXPANDABLE_%25E2%2582%25B950%252C000%2Bto%2B%25E2%2582%25B970%252C000_laptops-store_498d3f89-fa47-4e2a-bee1-6abdb3838038_DesktopSite_wp8&fm=neo%2Fmerchandising&iid=M_5617c17b-3f5e-4e77-8b78-bf4350031fa8_10.498d3f89-fa47-4e2a-bee1-6abdb3838038_DesktopSite&ppt=sp&ppn=sp&page='+str(FlipkartSpiderSpider.pgno)
        if FlipkartSpiderSpider.pgno <= 9:
            FlipkartSpiderSpider.pgno += 1
            yield scrapy.Request(url=next_page, callback = self.parse)