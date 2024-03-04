
Description: This Python program scrapes product data from the "Snatcher" website's beauty and lifestyle section and saves it to a CSV file.

Instructions:
1. Install the required libraries: `requests`, `BeautifulSoup`, and `pandas`. You can install them using pip:

2. Run the program:
- Copy the provided code into a Python file (e.g., `scrape_snatcher.py`).
- Execute the Python script in your terminal or preferred Python environment.

3. The program will start scraping product data from the specified URL (`https://snatcher.co.za/beauty-amp-lifestyle/beauty/?sort=bestselling&limit=100&mode=4`).
- It retrieves product names, prices, and ratings from the website.
- The scraping process continues until there are no more pages of products to scrape.

4. The scraped data is stored in a pandas DataFrame and then saved to a CSV file named `products.csv`.
- Each row in the CSV file represents a product, with columns for the product name, price, and rating.

5. Check the generated `products.csv` file to view the scraped product data.

Note:
- This program demonstrates web scraping techniques using Python libraries like requests and BeautifulSoup.
- Ensure that you comply with the website's terms of service and robots.txt file when scraping data.
- Customize the program according to your specific scraping needs or target website structure.
- Feel free to modify the program to handle errors, logging, or additional data processing as required.

Enjoy scraping data from the Snatcher website and analyzing the beauty and lifestyle products!
