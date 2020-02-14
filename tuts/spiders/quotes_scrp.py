import scrapy
from scrapy.http import FormRequest

main_url="https://studentportal.mku.ac.ke/umis/studentportal/"
fees_url='https://studentportal.mku.ac.ke/umis/studentportal/statement_detailed.php'
total_fees='https://studentportal.mku.ac.ke/umis/studentportal/course_reg_student.php'


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'https://studentportal.mku.ac.ke/umis/studentportal/course_registration.php',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):

        # print(response.body)
        # link_ex = response.xpath('//*[@class="item-482"]/a/text()').extract()
        # print(link_ex)
 
        return FormRequest.from_response(response,
                        formdata={'regNo':'dit/2019/44286',
                                    'smisPass':'35943144','smisLogon':'maybe'},
                        callback=self.scrape_p)

    def scrape_p(self,response):
        name_box = response.xpath('//div/div/div/p/text()').extract()
        total_fee_box = response.xpath('//tr/td/text()').extract()

        print(total_fee_box[-3])

        print(name_box[0])

        return scrapy.Request('https://studentportal.mku.ac.ke/umis/studentportal/statement_detailed.php', 
             callback = self.parse_page1)

    def parse_page1(self, response): 
        closing_balance=response.xpath('//tr/td/b/text()').extract()

        print(closing_balance[-1]) 


        