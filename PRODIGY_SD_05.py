
'''
Author : Joelle  K. Kuyula
Description: This is a web scraping program to extract products information from a specific website.
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://snatcher.co.za/beauty-amp-lifestyle/beauty/?sort=bestselling&limit=100&mode=4"
myData = {}
product_no = 0

while True:
    # Send a GET request to the URL
    response = requests.get(url)

    data = response.text

    # Parse HTML content
    soup = BeautifulSoup(data, 'html.parser')

    # Find all product items
    products = soup.find_all('li', {'class': 'product'})

    # Extract product names, prices, and ratings
    for product in products:
        name = product.find('h4').text.strip()
        price = product.find('div', {'class': 'card-text card-text--price'}).text.strip()
        rating_tag = product.find('div', {'data-average-rating': True})
        rating = rating_tag.text if rating_tag else 'N/A'
        product_no += 1
        myData[product_no] = [name, price, rating]

    url_tag = soup.find('a', {'class': 'next'})
    if url_tag:
        url = 'https://snatcher.co.za' + url_tag['href']
        print(url)
    else:
        break

# Create DataFrame from scraped data
myData_df = pd.DataFrame.from_dict(myData, orient='index', columns=['Name', 'Price', 'Rating'])


# Save DataFrame to CSV file
myData_df.to_csv('products.csv', index=False)




