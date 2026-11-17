
# Sales Data Analysis Using Python

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the sales dataset
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(BASE_DIR, "sales_data.csv"))
# Step 2: Display the dataset
print("SALES DATASET")
print(df)

# Step 3: Display basic information
print("\nDATASET INFORMATION")
print(df.info())

# Step 4: Check for missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Step 5: Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Step 6: Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nUPDATED SALES DATA")
print(df.head())

# Step 7: Calculate total revenue
total_revenue = df["Total_Sales"].sum()

print("\nTOTAL REVENUE: Rs.", total_revenue)

# Step 8: Calculate total quantity sold
total_quantity = df["Quantity"].sum()

print("TOTAL QUANTITY SOLD:", total_quantity)

# Step 9: Find best-selling products
product_sales = df.groupby("Product")[
    "Quantity"
].sum().sort_values(ascending=False)

print("\nPRODUCT-WISE SALES")
print(product_sales)

# Step 10: Calculate revenue by product
product_revenue = df.groupby("Product")[
    "Total_Sales"
].sum().sort_values(ascending=False)

print("\nPRODUCT-WISE REVENUE")
print(product_revenue)

# Step 11: Calculate monthly revenue
df["Month"] = df["Date"].dt.strftime("%B")

monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["Total_Sales"].sum()

print("\nMONTHLY SALES")
print(monthly_sales)

# Step 12: Calculate region-wise revenue
region_sales = df.groupby("Region")[
    "Total_Sales"
].sum().sort_values(ascending=False)

print("\nREGION-WISE SALES")
print(region_sales)

# Step 13: Display product-wise sales graph
plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 14: Display monthly revenue graph
plt.figure(figsize=(8, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 15: Display region-wise sales graph
plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar")

plt.title("Region-wise Sales Revenue")
plt.xlabel("Region")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\nSALES DATA ANALYSIS COMPLETED SUCCESSFULLY!")
