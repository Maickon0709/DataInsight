import os

import matplotlib.pyplot as plt
import pandas as pd


def load_data(filename):
    """Load sales data from an Excel file."""
    return pd.read_excel(filename, engine="openpyxl")


def clean_data(data):
    """Clean the dataset and calculate the total price of each sale."""
    data = data.copy()

    # Remove duplicated records
    data = data.drop_duplicates()

    # Remove cancelled invoices
    data = data[~data["InvoiceNo"].astype(str).str.startswith("C")]

    # Remove invalid quantities
    data = data[data["Quantity"] > 0]

    # Remove invalid prices
    data = data[data["UnitPrice"] > 0]

    # Remove rows without a product description
    data = data.dropna(subset=["Description"])

    # Calculate the total value of each transaction
    data["TotalPrice"] = data["Quantity"] * data["UnitPrice"]

    return data


def analyze_data(data):
    """Calculate the main sales indicators."""
    total_revenue = data["TotalPrice"].sum()

    total_quantity = data["Quantity"].sum()

    total_transactions = data["InvoiceNo"].nunique()

    average_ticket = total_revenue / total_transactions

    top_products = (
        data.groupby("Description")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    top_products_quantity = (
        data.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    country_revenue = (
        data.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    monthly_revenue = (
        data.assign(Month=data["InvoiceDate"].dt.to_period("M"))
        .groupby("Month")["TotalPrice"]
        .sum()
    )

    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "total_transactions": total_transactions,
        "average_ticket": average_ticket,
        "top_products": top_products,
        "top_products_quantity": top_products_quantity,
        "country_revenue": country_revenue,
        "monthly_revenue": monthly_revenue,
    }


def create_charts(data, output_folder="charts"):
    """Create sales charts and save them as PNG files."""
    os.makedirs(output_folder, exist_ok=True)

    monthly_revenue = (
        data.assign(Month=data["InvoiceDate"].dt.to_period("M"))
        .groupby("Month")["TotalPrice"]
        .sum()
    )

    plt.figure(figsize=(12, 6))
    monthly_revenue.plot(kind="line", marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue (£)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_folder, "monthly_revenue.png"),
        dpi=150,
    )
    plt.close()

    top_products = (
        data.groupby("Description")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    top_products.plot(kind="barh")
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue (£)")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_folder, "top_products.png"),
        dpi=150,
    )
    plt.close()

    country_revenue = (
        data.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    country_revenue.plot(kind="barh")
    plt.title("Top 10 Countries by Revenue")
    plt.xlabel("Revenue (£)")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_folder, "country_revenue.png"),
        dpi=150,
    )
    plt.close()


def main():
    """Run the complete DataInsight analysis."""
    filename = "data/Online Retail.xlsx"

    print("=" * 50)
    print("DATAINSIGHT - SALES ANALYTICS")
    print("=" * 50)
    print()

    # Load dataset
    data = load_data(filename)

    print(f"Original records: {len(data):,}")

    # Clean dataset
    data = clean_data(data)

    print(f"Records after cleaning: {len(data):,}")
    print()

    # Analyze dataset
    results = analyze_data(data)

    print("=" * 50)
    print("MAIN SALES INDICATORS")
    print("=" * 50)

    print(f"Total revenue: £{results['total_revenue']:,.2f}")
    print(f"Total items sold: {results['total_quantity']:,}")
    print(f"Total transactions: {results['total_transactions']:,}")
    print(f"Average ticket: £{results['average_ticket']:,.2f}")
    print()

    print("=" * 50)
    print("TOP 10 PRODUCTS BY REVENUE")
    print("=" * 50)

    for product, revenue in results["top_products"].items():
        print(f"{product}: £{revenue:,.2f}")

    print()

    print("=" * 50)
    print("TOP 10 PRODUCTS BY QUANTITY")
    print("=" * 50)

    for product, quantity in results["top_products_quantity"].items():
        print(f"{product}: {quantity:,}")

    print()

    print("=" * 50)
    print("TOP 10 COUNTRIES BY REVENUE")
    print("=" * 50)

    for country, revenue in results["country_revenue"].items():
        print(f"{country}: £{revenue:,.2f}")

    print()

    print("=" * 50)
    print("MONTHLY REVENUE")
    print("=" * 50)

    for month, revenue in results["monthly_revenue"].items():
        print(f"{month}: £{revenue:,.2f}")

    print()

    # Create charts
    create_charts(data)

    print("Charts created successfully in the 'charts' folder.")


if __name__ == "__main__":
    main()