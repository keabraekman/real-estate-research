import scrapy


class HomeAreaSpider(scrapy.Spider):
    name = "homearea"

    def start_requests(self):
        urls = [
            'https://www.homearea.com/place/new-york-city-new-york/3651000/',
            'https://www.homearea.com/place/panama-city-city-florida/1254700/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0'})

    def parse(self, response):
        city = response.url.split("/")[-3]
        filename = f'homearea-{city}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')