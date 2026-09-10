import pandas as pd

from project import load_data, clean_data, analyze_data


def test_load_data(tmp_path):
    """Test whether load_data correctly loads an Excel file."""
    file = tmp_path / "test.xlsx"

    original_data = pd.DataFrame(
        {
            "InvoiceNo": ["10001"],
            "StockCode": ["A001"],
            "Description": ["Test Product"],
            "Quantity": [2],
            "InvoiceDate": [pd.Timestamp("2011-01-01")],
            "UnitPrice": [10.0],
            "CustomerID": [12345],
            "Country": ["United Kingdom"],
        }
    )

    original_data.to_excel(file, index=False)

    result = load_data(file)

    assert len(result) == 1
    assert list(result.columns) == list(original_data.columns)


def test_clean_data():
    """Test whether clean_data removes invalid records."""
    data = pd.DataFrame(
        {
            "InvoiceNo": [
                "10001",
                "10001",
                "C10002",
                "10003",
                "10004",
                "10005",
            ],
            "StockCode": [
                "A001",
                "A001",
                "A002",
                "A003",
                "A004",
                "A005",
            ],
            "Description": [
                "Product A",
                "Product A",
                "Product B",
                "Product C",
                None,
                "Product E",
            ],
            "Quantity": [
                2,
                2,
                1,
                -5,
                3,
                4,
            ],
            "InvoiceDate": [
                pd.Timestamp("2011-01-01"),
                pd.Timestamp("2011-01-01"),
                pd.Timestamp("2011-01-02"),
                pd.Timestamp("2011-01-03"),
                pd.Timestamp("2011-01-04"),
                pd.Timestamp("2011-01-05"),
            ],
            "UnitPrice": [
                10.0,
                10.0,
                5.0,
                5.0,
                5.0,
                0.0,
            ],
            "CustomerID": [
                1,
                1,
                2,
                3,
                4,
                5,
            ],
            "Country": [
                "United Kingdom",
                "United Kingdom",
                "France",
                "Germany",
                "Spain",
                "Italy",
            ],
        }
    )

    result = clean_data(data)

    assert len(result) == 1
    assert result.iloc[0]["Description"] == "Product A"
    assert result.iloc[0]["TotalPrice"] == 20.0


def test_analyze_data():
    """Test whether analyze_data calculates the correct indicators."""
    data = pd.DataFrame(
        {
            "InvoiceNo": [
                "10001",
                "10002",
                "10003",
            ],
            "StockCode": [
                "A001",
                "A002",
                "A003",
            ],
            "Description": [
                "Product A",
                "Product B",
                "Product A",
            ],
            "Quantity": [
                2,
                3,
                1,
            ],
            "InvoiceDate": [
                pd.Timestamp("2011-01-01"),
                pd.Timestamp("2011-01-15"),
                pd.Timestamp("2011-02-01"),
            ],
            "UnitPrice": [
                10.0,
                5.0,
                10.0,
            ],
            "CustomerID": [
                1,
                2,
                3,
            ],
            "Country": [
                "United Kingdom",
                "France",
                "United Kingdom",
            ],
        }
    )

    data["TotalPrice"] = data["Quantity"] * data["UnitPrice"]

    result = analyze_data(data)

    assert result["total_revenue"] == 45.0
    assert result["total_quantity"] == 6
    assert result["total_transactions"] == 3
    assert result["average_ticket"] == 15.0

    assert result["top_products"]["Product A"] == 30.0
    assert result["top_products"]["Product B"] == 15.0

    assert result["country_revenue"]["United Kingdom"] == 30.0
    assert result["country_revenue"]["France"] == 15.0

    assert result["monthly_revenue"][pd.Period("2011-01")] == 35.0
    assert result["monthly_revenue"][pd.Period("2011-02")] == 10.0