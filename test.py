
import requests
from bs4 import BeautifulSoup

# Send a request to the news website


response = requests.get('https://news.google.com/search?q=bitcoin', headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.675 Safari/537.36"})

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')



# Find all news articles
articles = soup.find_all('article')

a = {
    
}
# Print the title and URL of each article
for article in articles:
    # with open("index.html", "a") as f:
    #     f.write(f"\n\n\n{article}")
    title = article.find('a', {"data-n-tid": "29"}).text
    url = article.find('a')['href']
    a.update({title:url})
    
    if len(a) == 50:
        break

print(len(a))
print(len(str(a)))