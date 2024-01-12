import requests
from bs4 import BeautifulSoup
from model_core import ModelGpt

class PriceAgent(ModelGpt):
    def __init__(self):
        self.role = "You are a useful assistant in analyzing the prices of cryptocurrencies"
        super().__init__()
    
    def get_news(self):
        response = requests.get('https://news.google.com/search?q=bitcoin', headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.675 Safari/537.36"})
        articles = BeautifulSoup(response.text, 'lxml').find_all('article')

        data = {}

        for article in articles:
            title = article.find('a', {"data-n-tid": "29"}).text
            url = article.find('a')['href']
            data.update({f"'News' {title}":url})
            if len(data) == 50:
                break
        return data
    
    def get_price(self):
        response = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart', params={
            'vs_currency': 'usd',
            'days': 7
        })

        data = response.json()

        current_price = data['prices'][-1][1]
        past_price = data['prices'][0][1]
        price_change = current_price - past_price

        return (
            f'Цена биткойна 7 дней назад: {past_price}'
            f'Текущая цена биткойна: {current_price}'
            f'Изменение цены биткойна за последние 7 дней: {price_change}'
        )
    
    def analyze_price(self, prompt):
        prompt = str(self.get_news()) + "\n\n" + self.get_price() + "\n\n" + prompt
        return self.get_request(self.role, prompt)
    
    
    def __str__(self) -> str:
        return f"Агент анализа цен Bitcoin"
    
priceagent = PriceAgent()
print(priceagent.analyze_price("На сколько изменилась цена биткойна за 7 дней? Объясни на основании новостей почему? пиши на русском"))

