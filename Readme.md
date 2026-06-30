# 📚 Ecommerce Product Scraper

A Python-based web scraping project that extracts product information from an e-commerce website, stores it in Excel and SQLite, visualizes product prices, and provides a simple Flask web interface for searching products.

## 🚀 Features

- Scrape product title, price, rating and link
- Export data to Excel
- Store data in SQLite Database
- Search products using Flask
- Price visualization using Matplotlib

## 🛠 Tech Stack

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite
- Flask
- Matplotlib

## 📂 Project Structure

```
Ecommerce-Scraper/
│
├── scraper.py
├── database.py
├── visualize.py
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│     index.html
│
└── static/
      chart.png
```

## ▶️ Installation

```bash
git clone <repository-url>

cd Ecommerce-Scraper

pip install -r requirements.txt
```

Run the scraper

```bash
python scraper.py
```

Create database

```bash
python database.py
```

Generate visualization

```bash
python visualize.py
```

Start Flask

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

## 📸 Output

- Product Search
- Product Table
- Price Visualization

## 👨‍💻 Author

Yash Kagra