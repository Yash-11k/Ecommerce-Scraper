import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all product cards
    books = soup.find_all("article", class_="product_pod")

    product_list = []

    for book in books:

        # Title
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Rating
        rating = book.find("p")["class"][1]

        # Product Link
        link = book.h3.a["href"]

        full_link = "https://books.toscrape.com/" + link

        product = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Link": full_link
        }

        product_list.append(product)

    # Convert into DataFrame
    df = pd.DataFrame(product_list)

    # Print data
    print(df)

    # Save Excel
    df.to_excel("products.xlsx", index=False)

    print("\nData saved successfully into products.xlsx")

else:
    print("Failed to connect.")