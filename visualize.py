import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("products.db")

# Read data
df = pd.read_sql_query("SELECT * FROM products", conn)

conn.close()

# Remove £ symbol and convert price to float
# df["Price"] = df["Price"].str.replace("£", "", regex=False).astype(float)
df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

# Create graph
plt.figure(figsize=(10,5))
plt.plot(df.index, df["Price"], marker="o")

plt.title("Book Prices")
plt.xlabel("Product Number")
plt.ylabel("Price (£)")

plt.grid(True)

# Save graph
plt.savefig("chart.png")

# Show graph
plt.show()

print("Chart saved as chart.png")

