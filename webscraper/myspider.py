import scrapy
import json

class SizeCharterSpider(scrapy.Spider):
  name = 'sizecharterspider'
  start_urls = ['http://www.sizecharter.com/brands']

  output_file = open("results.txt", "w");
  
  def parse(self, response):
    for chart in response.css('.chart'):
      store_name = response.css('main>h1::text').extract_first()
      for table in chart.css('table'):
        listofTrs = []
        for tr in table.css('tr'):
          l = tr.css('td ::text').re('^[^\n]*$')
          if len(l) > 0:
            listofTrs.append(l)
      
        jsonToWrite = {'store': store_name[0:len(store_name)-12],
               'title': chart.css('h2 ::text').extract(),
               'headings': table.css('thead>tr>th::text').extract(),
               'table': listofTrs}
        json.dump(jsonToWrite, self.output_file)
        self.output_file.write("\n")        
  
    for link in response.css('#list>li>a'):
      yield response.follow(link, self.parse)
