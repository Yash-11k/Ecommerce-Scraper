import pandas as pd
import sqlite3

# Read Excel file
df = pd.read_excel("products.xlsx")

# Connect to SQLite database
conn = sqlite3.connect("products.db")

# Save DataFrame into database
df.to_sql("products", conn, if_exists="replace", index=False)

print("Data saved successfully into products.db")

# Close connection
conn.close()